#is operator
x=10
y=10
z=x
c=5
d=10

print(x is y) #true means sam ememory location(reference or instance),it is mostly used in datastructures. value is not same memory location is same
print(x is c) 
print(x is z)
print(y is z)
print(y is x)
print(c is x)
print(c is c)
print(c is d)
print(x is d)

x=[3,4,5]
y=[3,4,5]
z=x

print(x is y)#false
print(x is z)#true
print(z is y)#false