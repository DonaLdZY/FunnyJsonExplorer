from abc import ABC, abstractmethod

from node import RootNode, ConfigurableNode
from strategy import ConfigurableDrawStrategy

        
class FactoryRegistry:
    def __init__(self):
        self._factories = {}

    def register_factory(self, factory_type, factory_instance):
        if not issubclass(factory_instance.__class__, NodeFactory):
            raise ValueError("Factory instance must be a subclass of NodeFactory")
        self._factories[factory_type] = factory_instance

    def get_factory(self, factory_type):
        factory = self._factories.get(factory_type)
        if factory is None:
            raise ValueError(f"No factory registered for type: {factory_type}")
        return factory

class NodeFactory(ABC):

    @staticmethod
    def create_root_Node():
        return RootNode()

    @abstractmethod
    def create_Node(self, icon_factory, name, is_top, is_bottom):
        pass

    @abstractmethod
    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        pass


class ConfigurableFactory(NodeFactory):
    def __init__(self, style_name, config_file='config/style_config.json'):
        super().__init__()
        self.style_name = style_name
        self.config_file = config_file

    def create_Node(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableNode(icon_factory.get_icon(is_leaf=False), name, is_top, is_bottom, False,
                                     ConfigurableDrawStrategy(), self.style_name, self.config_file)

    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableNode(icon_factory.get_icon(is_leaf=True), name, is_top, is_bottom, True,
                                     ConfigurableDrawStrategy(), self.style_name, self.config_file)


class TreeFactory(ConfigurableFactory):
    def __init__(self):
        super().__init__("tree")


class RectangleFactory(ConfigurableFactory):
    def __init__(self):
        super().__init__("rectangle")
