from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit(self, component):
        return 0


class DrawVisitor(Visitor):
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.prefix = []

    def set_prefix(self, new_prefix):
        self.prefix = new_prefix

    def visit(self, component):
        component.draw(self.maxlength, self.prefix)
