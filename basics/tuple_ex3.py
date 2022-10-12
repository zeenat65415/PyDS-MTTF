#tuple with mixed datatypes
my_tuple=(1,"Hello",3.4)
print(my_tuple)

#Nested Tuple
my_tuple=("mouse",[8,4,6],(1,2,3))
print(my_tuple)


#tuple-set-list(interchangeable)
x=[2,3,4,5,5,6,6,7]
xt=tuple(x)#list->tuple
xl=list(x)#tuple->list
xs=set(x)#list->set
xl=list(xs)#set->list
xs=set(xt)#tuple->set
xt=tuple(xs)#set->tuple

#WAP to create a tuple,by taking ten inputs from the user(directly cannot be appended in numbers() as shown in tuple_no_append.py)
numbers=[]                                                    
for i in range(10):                                          
    v=(input("enter a number:"))                          
    numbers.append(v)                                    
print("numbers entered by a user:",numbers)      
xt=tuple(numbers)    
print(xt)    


#Accessing tuple elements using indexing
my_tuple=('p','e','r','m','i','t')
print(my_tuple[0]) #'p'
print(my_tuple[5]) #'t'
n_tuple=("mouse",[8,4,6],(1,2,3))#nested tuple
print(n_tuple[0][3]) #nested index 's'
print(n_tuple[1][1]) #'4'

#slicing(Accessing tuple elements using slicing)
my_tuple=('e','x','c','a','l','i','b','u','r')

#elements second to fourth
#Output:('x','c','a')
print(my_tuple[1:4])

#elements begining to second
#Output:('e','x')
print(my_tuple[:-7])

#elements 8th to end
#Output:('u','r')
print(my_tuple[7:])

#elements begining to end
print(my_tuple[:])


#Other Operations

#Concatenation
#Output:(1,2,3,4,5,6)
print((1,2,3)+(4,5,6))

#Repeat
#Output:('Repeat','Repeat','Repeat')
print(('Repeat',)*3)

