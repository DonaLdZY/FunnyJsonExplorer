from abc import ABC, abstractmethod

from Node import TemplateNode,Node
from Strategy import TemplateNodeDrawStrategy,RootNodeDrawStrategy

        
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

    @abstractmethod
    def create_root_node(self):
        pass

    @abstractmethod
    def create_node(self, icon_factory, name, is_top, is_bottom):
        pass

    @abstractmethod
    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        pass


class TemplateNodeFactory(NodeFactory):
    def __init__(self, style_name, config_file='config/style_config.json'):
        super().__init__()
        self.style_name = style_name
        self.config_file = config_file
        
    def create_root_node(self):
        return Node(RootNodeDrawStrategy())

    def create_node(self, icon_factory, name, is_top, is_bottom):
        return TemplateNode(TemplateNodeDrawStrategy(), icon_factory.get_icon(is_leaf=False), name, 
                                is_top, is_bottom, False, self.style_name, self.config_file)

    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        return TemplateNode(TemplateNodeDrawStrategy(), icon_factory.get_icon(is_leaf=True), name, 
                                is_top, is_bottom, True, self.style_name, self.config_file)


class TreeFactory(TemplateNodeFactory):
    def __init__(self):
        super().__init__("tree")


class RectangleFactory(TemplateNodeFactory):
    def __init__(self):
        super().__init__("rectangle")
