nums=[1,2,3,4,1,2,3,5,6,7,3,3,2,1,2,3,5,6]
names=['Ajay Singh','Vijay Pratap','Gunja Thakur' ]

num_sqr = list(map(lambda i:i** 2,nums))
print(num_sqr)

num_eq1=list(map(lambda i: i+4* i**2,nums))
print(num_eq1)

first_names=tuple(map(lambda nm: nm.split()[0],names))
print(first_names)