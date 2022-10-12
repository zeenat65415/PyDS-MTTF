#Tuples are immutable,"immutable" means cannot be changed at  runtime.
#list is used in dynamic programming,as list are mutable.
# Dynamic Programming- is used where we have problems,which can be divided into similar sub-problems.So that there results can be re-used.
#  ex of Dynamic Programming-Tower of Hanoi PUzzle
#                           -Dijkstra's   algorithm for shortest path problem. 
#                           -Egg Dropping puzzle
#                           -MCM(Matrix Chain Multiplication)  
   
#python default datatype is tuple.
a=1,2,3,4#type=>tuple
print(a)
print(type(a))
#Therefore a Tuple can be created without using parenthesis.This is known as tuple packing.
my_tuple=3,4,6,"Apple"
print(my_tuple,type(my_tuple))

#bonus content
x,*y=1,2,3,4,5,6
print(x,y)
print(type(x),type(y))

x,y,*z=1,2,3,4,5,6
print(x,y,z)
print(type(x),type(y),type(z))

#back to tuple

x=(23,45,21,45)
y=tuple([3,2,1,5])#converting a list to tuple

print(x,y)
print(type(x),type(y))