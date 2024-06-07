from utils import load_json
from Visitor import DrawVisitor

MAX_LENGTH = 40


class FunnyJsonExplorer:
    def __init__(self, node_factory, icon_factory):
        self.node_factory = node_factory
        self.icon_factory = icon_factory

    def show(self, json_file):
        data = load_json(json_file)
        root_node = self.node_factory.create_root_node()
        self.parse_json(data, root_node)
        draw_visitor = DrawVisitor(MAX_LENGTH)
        root_node.accept(draw_visitor)

    def parse_json(self, data, root_node, is_top=True, is_bottom=True):
        for i, (key, value) in enumerate(data.items()):
            if isinstance(value, dict):
                sub_node = self.node_factory.create_node(self.icon_factory, key, (is_top and (i==0)), False)
                root_node.add(sub_node)
                self.parse_json(value, sub_node, False, is_bottom and (i == len(data.items()) - 1))
            else:
                if value is not None:
                    key = f"{key}: {value}"
                leaf = self.node_factory.create_leaf(self.icon_factory, key, (is_top and (i==0)), (is_bottom and (i == len(data.items()) - 1)))
                root_node.add(leaf)
