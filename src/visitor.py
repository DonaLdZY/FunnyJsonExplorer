from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, component):
        pass

class DrawVisitor(Visitor):
    def __init__(self,maxlength):
        self.maxlength=maxlength
        self.prefix=[]
        
    def setPrefix(self, newprefix):
        self.prefix=newprefix
        
    def visit(self, component):
        component.draw(self.maxlength,self.prefix)
