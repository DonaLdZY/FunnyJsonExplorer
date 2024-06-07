from abc import ABC, abstractmethod

from container import RootContainer, ConfigurableContainer
from strategy import ConfigurableDrawStrategy

        
class FactoryRegistry:
    def __init__(self):
        self._factories = {}

    def register_factory(self, factory_type, factory_instance):
        if not issubclass(factory_instance.__class__, ContainerFactory):
            raise ValueError("Factory instance must be a subclass of ContainerFactory")
        self._factories[factory_type] = factory_instance

    def get_factory(self, factory_type):
        factory = self._factories.get(factory_type)
        if factory is None:
            raise ValueError(f"No factory registered for type: {factory_type}")
        return factory

class ContainerFactory(ABC):

    @staticmethod
    def create_root_container():
        return RootContainer()

    @abstractmethod
    def create_container(self, icon_factory, name, is_top, is_bottom):
        pass

    @abstractmethod
    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        pass


class ConfigurableFactory(ContainerFactory):
    def __init__(self, style_name, config_file='config/style_config.json'):
        super().__init__()
        self.style_name = style_name
        self.config_file = config_file

    def create_container(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableContainer(icon_factory.get_icon(is_leaf=False), name, is_top, is_bottom, False,
                                     ConfigurableDrawStrategy(), self.style_name, self.config_file)

    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableContainer(icon_factory.get_icon(is_leaf=True), name, is_top, is_bottom, True,
                                     ConfigurableDrawStrategy(), self.style_name, self.config_file)


class TreeFactory(ConfigurableFactory):
    def __init__(self):
        super().__init__("tree")


class RectangleFactory(ConfigurableFactory):
    def __init__(self):
        super().__init__("rectangle")
