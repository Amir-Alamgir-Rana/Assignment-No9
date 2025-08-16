# abstraction program
from abc import abstractmethod


class Genernal_inf():
    @abstractmethod
    def __init__(self,gender,salary):
        self.gender=gender
        self.salary=salary
class amir(Genernal_inf):
 def polymorphism(self):
    print("This is method is related to amir")
class asad(Genernal_inf):
 def polymorphism(self):
    print("This is method is related to asad ")

a=amir(gender="M",salary=20000)
a.polymorphism()
print(a.gender,a.salary)

b=asad(gender="M",salary=30000)
b.polymorphism()
print(b.gender,b.salary)