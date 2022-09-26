#tuple_set_list(interchangeable)

x=[2,3,4,5,5,6,6,7]
xt=tuple(x)#list->tuple
xl=list(xt)#tuple->list
xs=set(x)#list->set
xl=list(xs)#set->list
xs=set(xt)#tuple->set
xt=tuple(xs)#set->tuple
#wap to create a tuple,by taking ten inputs from the user
numbers=[]                                                    
for i in range(10):                                          
    v=int(input("enter a number:"))                          
    numbers.append(v)                                    
print("numbers entered by a user:",numbers)      
xt=tuple(numbers)    
print(xt)    


#slicing
my_tuple=('e','x','c','a','l','i','b','u','r')

print(my_tuple[1:4])

