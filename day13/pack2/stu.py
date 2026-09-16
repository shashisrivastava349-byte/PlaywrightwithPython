class Student:
    def __init__(self,id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    def displaystu(self):
        print("stuid:{} stuname:{} stugrade:{}".format(self.id,self.name,self.grade))