#Example 1:
class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0      #private variable __marks

    #getter method
    def get_marks(self):
        return self.__marks

    #Setter method
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("marks error. Marks must be <=100")
#Usage
stu=Student("John")
stu.set_marks(99)
print(stu.get_marks())

