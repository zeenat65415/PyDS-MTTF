#Required and default parameter   
   
    # default parameter must come after required parameter
# def total( b=3,c=0,a):#SyntaxError: non-default argument follows default argument
#     return a + b + c

def total(a, b=3,c=0):
    return a + b + c

# named parameters must come after positional parameter 
print(total(5)) #if no arguement passed then TypeError: total() missing 1 required positional argument: 'a'   
print(total(a=5))

print(total(100,50))
print(total(a=100,b=50))
print(total(b=50,a=100)) # swapped and working

print(total(10,10,10))
print(total(a=10,c=10,b=10))
print(total(b=10,a=10,c=10))
print(total(b=10,c=10,a=10))
print(total(a=10,c=10,b=10))
print(total(10,c=10,b=10))
# print(total(c=10,b=10,10))#error-SyntaxError: positional argument follows keyword argument

# polymorphism-in python, polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.


