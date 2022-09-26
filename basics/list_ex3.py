x=[1,2,3,1,2,2,3,3,1,1,2,3,3,3,1,1,1,2,3,3,3,1,4,1,1,2,2,2]

x_one=x.count(1)
x_two=x.count(2)
x_four=x.count(4)
x_five=x.count(5)
print('1 occured',x_one,'times')
print('2 occured',x_two,'times')
print('4 occured',x_four,'times')
print('5 occured',x_five,'times')

y=[23,45,6,2,21,22,32,23]
z=[1,3,5,6,1]

print('x adding y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)

xyz=x+y+z
print(xyz)

a=['apple','banana','cherry','dragonfruit','elaichi']
v=a.pop(3)#pop can remove value from an index
print(a)
print(v)
lv=a.pop()#pop removes last value by deafault
print(a)
print(lv)