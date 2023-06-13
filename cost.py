"""
this class define the costs that we have.

"""

from abc import ABC, abstractmethod

class Cost(ABC):

    @abstractmethod
    def show_the_object(self):
        pass


class ComplexCost(Cost):

    def __init__(self, price):
        self.price = price

    def show_the_object(self):
        return(f"the Complex cost is, {self.price}")


class BlockCost(Cost):

    def __init__(self, price):
        self.price = price

    def show_the_object(self):
        return(f"the Block cost is, {self.price}")


class FloorCost(Cost):

    def __init__(self, price):
        self.price = price

    def show_the_object(self):
        return(f"the Floor cost is, {self.price}")


class UnitCost(Cost):

    def __init__(self, price):
        self.price = price

    def show_the_object(self):
        return(f"the Unit cost is, {self.price}")