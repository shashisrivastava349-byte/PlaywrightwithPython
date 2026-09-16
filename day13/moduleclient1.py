#Approach 1:
# import pack1.module1
# import pack1.module2
#
# pack1.module1.display()
# pack1.module2.show()

#Approach 2:
# from pack1.module1 import *
# from day13.pack1.pack2.module2 import *
# display()
# show()

#If we have to access subpackage
#Approach 1:
# import pack1.module1
# import pack1.pack2.module2
#
# pack1.module1.display()
# pack1.pack2.module2.show()

#Approach 2:
# from pack1 import module1
# from pack1.pack2 import module2
#
# module1.display()
# module2.show()

#Approach 3:
from pack1.module1 import *
from pack1.pack2.module2 import *

display()
show()












