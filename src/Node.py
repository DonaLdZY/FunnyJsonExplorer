import os

from iterator import NodeIterator
from utils import load_json


class RootNode:
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, max_length, prefix):
        pass

    def accept(self, visitor):
        visitor.visit(self)
        iterator = NodeIterator(self)
        prefix = visitor.prefix[:]
        while iterator.has_next():
            child = iterator.next()
            new_prefix = prefix + [iterator.has_next()]
            visitor.set_prefix(new_prefix)
            child.accept(visitor)


class Node(RootNode):
    def __init__(self, icon, name, is_top, is_bottom, is_leaf, draw_strategy):
        super().__init__()
        self.icon = icon
        self.name = name
        self.is_top = is_top
        self.is_bottom = is_bottom
        self.is_leaf = is_leaf
        self.draw_strategy = draw_strategy

    def draw(self, max_length=0, prefix=None):
        if prefix is None:
            prefix = []
        self.draw_strategy.draw(self, max_length, prefix)


class ConfigurableNode(Node):
    def __init__(self, icon, name, is_top, is_bottom, is_leaf, draw_strategy, style_name,
                 config_file='config/style_config.json'):
        super().__init__(icon, name, is_top, is_bottom, is_leaf, draw_strategy)
        self.style_name = style_name
        self.config_file = config_file

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ValueError(f"Config file not found: {self.config_file}")
        config = load_json(self.config_file)
        if self.style_name not in config:
            raise ValueError(f"Unknown style: {self.style_name}")
        style = config[self.style_name]
        line_type = "top" if self.is_top else ("bottom" if self.is_bottom else "body")
        if line_type not in style:
            raise ValueError(f"Incomplete style: {self.style_name} style doesn't have {line_type} line config")
        return style[line_type]
