from abc import ABC, abstractmethod

from container import RootContainer, ConfigurableContainer
from strategy import ConfigurableDrawStrategy


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
