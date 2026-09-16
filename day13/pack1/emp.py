class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def displayemp(self):
        print("empid:{} empname:{} salary:{}".format(self.id, self.name, self.salary))
