import sys

from pack2.stu import Student

sys.path.append("D:/Playwright_Python/day13/pack1")

from emp import Employee
myemp=Employee(101, "John", 500)
myemp.displayemp()

sys.path.append("D:/Playwright_Python/day13/pack2")
mystu=Student(101,"John", "A")
mystu.displaystu()