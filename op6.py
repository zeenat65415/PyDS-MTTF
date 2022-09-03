#is operator
x=10
y=10
z=x
c=5
d=10

print(x is y) #True means same mememory location(reference or instance),it is mostly used in datastructures. value is not same memory location is same
print(x is c) #False
print(x is z)#True
print(y is z)#True
print(y is x)#True
print(c is x)#False
print(c is c)#True
print(c is d)#False
print(x is d)#True

x=[3,4,5]#it is a list here x can not be equal to y as there can be many different operations that can be performed on list x and y
y=[3,4,5]
z=x

print(x is y)#False
print(x is z)#True
print(z is y)#False