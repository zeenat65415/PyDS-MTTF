name=input("Enter your name:")
college=input("Where do you study:")
city=input("City Name:")
age=input("Enter your age:")
animal=input("National animal of India:")

print(name,college,city,age,animal)
print(type(name))
print(type(college))
print(type(city))
print(type(age))
print(type(animal))#dataype by default is string(to conver we do typecasting)
#we use various typecasting fn
#int(),str(),float(),bool(),list(),tuple(),set(),dict()

age= int(age)#typecasting
print(age,type(age))


a=input('enter a number=>')
b=input('enter a number=>')

print(a+b)#2131
print(type(a),type(b))#str
a=int(a)#typecasting
b=int(b)#typecasting
print(a+b)#52
print(type(a))
print(type(b))
