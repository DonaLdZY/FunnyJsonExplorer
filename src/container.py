import os
from abc import abstractmethod

from utils import load_json


class RootContainer:
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, max_length, prefix=[]):
        for i, child in enumerate(self.children):
            new_prefix = prefix[:] + [(i < len(self.children) - 1)]
            child.draw(new_prefix, max_length)


class Conttainer:
    def __init__(self, icon, name, is_top, is_bottom, is_leaf):
        self.icon = icon
        self.name = name
        self.is_top = is_top
        self.is_bottom = is_bottom
        self.is_leaf = is_leaf
        self.children = []

    def add(self, component):
        self.children.append(component)

    @abstractmethod
    def draw(self, max_length=0, prefix=[]):
        pass


class ConfigableConttainer(Conttainer):
    def __init__(self, icon, name, is_top, is_bottom, is_leaf, style_name,
                 config_file='config/style_config.json'):
        super().__init__(icon, name, is_top, is_bottom, is_leaf)
        self.style_name = style_name
        self.config_file = config_file

    def loadConfig(self):
        if not os.path.exists(self.config_file):
            raise ValueError(f"ConfigFile not found: {self.style_name}")
        config = load_json(self.config_file)

        if self.style_name not in config:
            raise ValueError(f"Unknown style: {self.style_name}")
        style = config.get(self.style_name)

        line_type = "top" if self.is_top else ("bottom" if self.is_bottom else "body")
        if line_type not in style:
            raise ValueError(f"Incomplete style: {self.style_name} style doesn't have {line_type} line config")
        tab_table = style.get(line_type)

        return tab_table

    def draw(self, prefix, max_length):
        tab_table = self.loadConfig()
        printbuffer = ""
        for i in range(len(prefix)):
            tab = tab_table.get("start" if i == 0 else "follow", {"?": "?"})
            c = "?"
            if (i < len(prefix) - 1):
                c = tab.get("opening" if prefix[i] else "lasting", "?")
            else:
                c = tab.get("open" if prefix[i] else "last", "?")
            printbuffer += c

        printbuffer += self.icon
        printbuffer += self.name

        while (len(printbuffer) < max_length - 1):
            printbuffer += tab_table.get("padding", "?")
        printbuffer += tab_table.get("end", "?")

        print(printbuffer)

        for i, child in enumerate(self.children):
            new_prefix = prefix[:] + [(i < len(self.children) - 1)]
            child.draw(new_prefix, max_length)
