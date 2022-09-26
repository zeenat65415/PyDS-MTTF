for i in range(100):
 print("Hii")

for i in range(100):
    print("Hello",i)


for i in range(100):
    print(i,end=",")

#start stop
for i in range(10,21):
    print(i,end=" x ")

#start stop
for i in range(10,21):
    print(i,end='😴')    


#step or gap value
for i in range( 1,11,2):
    print(i,end=" o ")  

# reverse loop
for i in range(10,0,-1):
    print(i,end=",")    


# enumerate is used for traversal not for repitition
data=[2,2,4,6,4,3,1,2,2,3,5]
for i,d in enumerate(data):
    print(i,d)
    print("=>")

print('=>')
data=[2,2,4,6,4,3,1,2,2,3,5]
for i,d in enumerate(data):
    print(i,d)

print("=>")
data=["apple","cherry","guava","banana","samosa"]
for i,d in enumerate(data):
    print(i,d)

print("=>")
data=["apple","cherry","guava","banana","samosa"]   
for i,d in enumerate(data):
    print(i+1,d)

data=["apple","cherry","guava","baana","samosa"]
for i in enumerate(data):
    print(i)    

#zip()
names=["Laptop","Mobile","Keyboard"]
prices=[59999,25000,299]
for n,p in  zip(names,prices):
    print(f"{n}=>${p}")   

names=["Apple","Banana","Cherry"]
price=[100,40,65]
for n,p in(names,price):
    print(f"{n}=>${p}")