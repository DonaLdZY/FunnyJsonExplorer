from utils import load_json
from visitor import DrawVisitor

MAX_LENGTH = 40


class FunnyJsonExplorer:
    def __init__(self, container_factory, icon_factory):
        self.container_factory = container_factory
        self.icon_factory = icon_factory

    def show(self, json_file):
        data = load_json(json_file)
        root_container = self.container_factory.create_root_container()
        self.parse_json(data, root_container)
        draw_visitor = DrawVisitor(MAX_LENGTH)
        root_container.accept(draw_visitor)

    def parse_json(self, data, container, is_top=True, is_bottom=True):
        for i, (key, value) in enumerate(data.items()):
            if isinstance(value, dict):
                sub_container = self.container_factory.create_container(self.icon_factory, key, is_top, False)
                container.add(sub_container)
                self.parse_json(value, sub_container, False, is_bottom and (i == len(data.items()) - 1))
            else:
                if value is not None:
                    key = f"{key}: {value}"
                leaf = self.container_factory.create_leaf(self.icon_factory, key, is_top,
                                                          (is_bottom and (i == len(data.items()) - 1)))
                container.add(leaf)
            is_top = False
