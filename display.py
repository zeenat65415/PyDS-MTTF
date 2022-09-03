name="Zeenat"
age=21

print(name,age)
# print(name+age) will give error as we can not add two different datatypes i.e., string and integer together. We have to do typecasting.
print(name+str(age))

#my name is Zeenat and I am 21 years old

#1 comma  separation 
print("My name is",name,'and I am',age,'years old')#comma means space
print("My name is",name,'and I am',age,'years old',sep='😴')
print("My name is ",name, "and I am", age,"years old",sep="   ")

#2 f-sting(important)it can format or manipulate data,gives better control and flexibility
print(f'My name is {name} and I am {age} years old')
print(f'My name is {name} \n and I am {age} years old')




