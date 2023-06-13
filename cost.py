"""
this class define the costs that we have.

"""

from abc import ABC, abstractmethod

class Cost(ABC):

    def __init__(self, price):
        self.price = price  #remove and get in the child class

    @abstractmethod
    def show_the_object(self):
        pass


class Complex(Cost):

    def show_the_object(self):

        return(f"the Complex cost is, {self.price}")


class Block(Cost):

    def show_the_object(self):

        return(f"the Block cost is, {self.price}")


class Floor(Cost):

    def show_the_object(self):

        return(f"the Floor cost is, {self.price}")


class Unit(Cost):

    def show_the_object(self):

        return(f"the Unit cost is, {self.price}")