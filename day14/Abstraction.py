#ABC - Abstract Base Class
#Example 1:
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    #Concrete class (implemented abstract methods from abstract class)
class Car(Vehicle):
    def start(self):
        print("car start")
    def stop(self):
        print("car stop")

#v=Vehicle() we can not create object of abstract class
c=Car()
c.start()
c.stop()