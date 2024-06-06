from abc import ABC, abstractmethod

class DrawStrategy(ABC):
    @abstractmethod
    def draw(self, component, max_length, prefix):
        pass
    
class RootDrawStrategy(DrawStrategy):
    def draw(self, component, max_length, prefix):
        pass
    
class ConfigableDrawStrategy(DrawStrategy):
    def draw(self, component, max_length, prefix):
        tab_table = component.load_config()
        printbuffer = ""
        for i in range(len(prefix)):
            tab = tab_table.get("start" if i == 0 else "follow", {"?": "?"})
            c = "?"
            if i < len(prefix) - 1:
                c = tab.get("opening" if prefix[i] else "lasting", "?")
            else:
                c = tab.get("open" if prefix[i] else "last", "?")
            printbuffer += c

        printbuffer += component.icon
        printbuffer += component.name

        while len(printbuffer) < max_length - 1:
            printbuffer += tab_table.get("padding", "?")
        printbuffer += tab_table.get("end", "?")

        print(printbuffer)
