from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ContainerIterator(Iterator):
    def __init__(self, container):
        self._container = container
        self._index = 0

    def next(self):
        if self.has_next():
            result = self._container.children[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def has_next(self):
        return self._index < len(self._container.children)
