#defining strings in python
#all of the following are equivalent
my_string='Hello'
print(my_string)
my_string="Hello"
print(my_string)
my_string='''Hello'''
print(my_string)
#triple quotes strings can be extended to multiple lines
my_string='''hello welcome to the 
world of python'''
print(my_string)

a="EXCALIBUR"
print(a)

b="Smallfoot"
print(b)

c='''Once upon a time,
there was a person 
that used to sleep.
The end '''
print(c)

print(a[0])#first character
print(a[2])#third character
print(a[-1])#last character
print(a[-3])#third last character

print(a[0],a[2],a[3])#first ,third ,fourth char

#getting a slice
s="digipodium"
slice1=s[4:7]
print(slice1)

name="Vijay Deenanath Chauhan"
for i,c in enumerate(name):
    print(i,c)


mname=name[6:-8]#Middle name
print(mname)
print(name[6:-8])
fname=name[:5]
print(fname)
lname= name[-7:]
print(lname)
name1=name[11:15]
print(name1)

#reversing the string
print(name[::-1])

print(name[:5][::-1])#reversing only first name


#every even index char
print(name[::2])#vjy

#every odd index char
print(name[1::2])

x=chr(65)
print(x)

x=chr(2365)
print(x)

x=chr(12365)
print(x)

# for i in range(200,15000):
#     print(i,chr(i))

# for i in range(15000,20000):
#     print(i,chr(i))

for i in range(65,70): #65 to 69
    print(i,chr(i))

y=ord("A")#ordinal
print(y,chr(y))#65
y=ord("a")
print(y)#97
y=ord("{")
print(y) #123   

#concatenation
w1="This"
w2="is"
w3="amazing"
msg=w1+w2 +w3
print(msg)

a="apple"
b="juice"
ab=a+b
print(ab)

#adding space between strings
msg=w1+" "+w2+" "+w3
print(msg)

#duplication
word="Hii"
print(word*3)

word="Hi "
print(word*3)

print("-"*88)

print("-"*25)