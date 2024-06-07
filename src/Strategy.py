from abc import ABC, abstractmethod


class DrawStrategy(ABC):
    @abstractmethod
    def draw(self, component, max_length, prefix):
        pass


class RootNodeDrawStrategy(DrawStrategy):
    def draw(self, component, max_length, prefix):
        pass


class TemplateNodeDrawStrategy(DrawStrategy):
    def draw(self, component, max_length, prefix):
        tab_table = component.load_config()
        print_buffer = ""
        for i in range(len(prefix)):
            tab = tab_table.get("start" if i == 0 else "follow", {"?": "?"})
            c = "?"
            if i < len(prefix) - 1:
                c = tab.get("opening" if prefix[i] else "lasting", "?")
            else:
                c = tab.get("open" if prefix[i] else "last", "?")
            print_buffer += c

        print_buffer += component.icon
        print_buffer += component.name

        while len(print_buffer) < max_length - 1:
            print_buffer += tab_table.get("padding", "?")
        print_buffer += tab_table.get("end", "?")

        print(print_buffer)
