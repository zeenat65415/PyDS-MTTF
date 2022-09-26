#immutable means cannot be changed at  runtime.
#list is used in dynamic programming.
#python default data type is tuple
a=1,2,3,4#type=>tuple
print(a)
print(type(a))

x,y,*z=1,2,3,4,5,6
print(x,y,z)
print(type(x),type(y),type(z))

x=(23,45,21,45)
y=tuple([3,2,1,5])#converting a list to tuple

print(x,y)
print(type(x),type(y))

#there are 11 functions in list
#tuple have two function
x=(1,2,3,1,2,3,1,2,3,1,1,1,2,3,3,3,3,1,1)

print('3 occurs=>',x.count(3))
print('3 occurs=>',x.count(3))
print('3 occurs=>',x.count(3))

y=(2,13,14,12,13)
print("556 found at =>",y.index(556))
print("32 found at=>",y.index(32))
print("12 found at=>",12)