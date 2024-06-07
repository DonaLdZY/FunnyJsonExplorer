from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def next(self):
        return 0

    @abstractmethod
    def has_next(self):
        pass


class NodeIterator(Iterator):
    def __init__(self, Node):
        self._node = Node
        self._index = 0

    def next(self):
        if self.has_next():
            result = self._node.children[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def has_next(self):
        return self._index < len(self._node.children)
