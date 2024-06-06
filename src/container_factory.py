from abc import ABC, abstractmethod

from container import RootContainer, ConfigurableContainer
from strategy import ConfigableDrawStrategy

class ContainerFactory(ABC):
    
    def create_root_container(self):
        return RootContainer()

    @abstractmethod
    def create_container(self, icon_factory, name, is_top, is_bottom):
        pass

    @abstractmethod
    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        pass


class ConfigableFactory(ContainerFactory):
    def __init__(self, style_name, config_file='config/style_config.json'):
        super().__init__()
        self.style_name = style_name
        self.config_file = config_file

    def create_container(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableContainer(icon_factory.get_icon(is_leaf=False) , name, is_top, is_bottom, False, ConfigableDrawStrategy(), self.style_name, self.config_file)

    def create_leaf(self, icon_factory, name, is_top, is_bottom):
        return ConfigurableContainer(icon_factory.get_icon(is_leaf=True), name, is_top, is_bottom, True, ConfigableDrawStrategy(), self.style_name, self.config_file)


class TreeFactory(ConfigableFactory):
    def __init__(self):
        super().__init__("tree")


class RectangleFactory(ConfigableFactory):
    def __init__(self):
        super().__init__("rectangle")
