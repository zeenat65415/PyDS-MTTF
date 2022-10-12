#WAP to create a tuple by taking ten inputs from the user.
x = ()

for i in range(10):
    n = input("Enter a value::")
    x.append(n)

print("The value entered were",x)
# AttributeError: 'tuple' object has no attribute 'append'