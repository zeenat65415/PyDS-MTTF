from helper import read

data= read("pride_n_prejudice.txt")

print(len(data))

newData=data[3:53]
print(newData)


for i,c in enumerate(newData):
 print(i,c)


#...
# formatting functions
#-lower
#-upper
#-swapcase
#-capitalize
#-title
#-casefold

# Allignment functions
#-ljust   
#-rjust
#-center

print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.capitalize())
print(newData.title())
print(newData.casefold())

word="Hello World"
spacing=20
ljust=word.ljust(spacing,"*")
print(ljust)
rjust=word.rjust(spacing,"-")
print(rjust)
cen=word.center(spacing,"💢")
print(cen)

word="Hello"
spacing=20
ljust=word.ljust(spacing,"*")
print(ljust)
rjust=word.rjust(spacing,"-")
print(rjust)
cen=word.center(spacing,"💢")
print(cen)

#validation functions-either true or false
print(newData.isupper())
print(newData.islower())
print(newData.isalpha())#since space is present and it is a special character the ans is False
print(newData.isnumeric())
print(newData.isalnum())
print(newData.isdigit())

#utitility functions
idx=newData.find("pride")#Pride in uppercase
if idx==-1:#For the user to undedrstand ,This handles the error in case the word is not found .
    print("Not found")
else:
    print(f'''pride is 
    found at index {idx}''')

idx2=newData.index("Pride")    
print(idx2)  


# idx5=newData.index("in")
# print(f"in is found at index {idx5}")#index where first"in"is found

idx5=data.index("in")
print(f"in is found at index{idx5}")

sentence="I am  living in Uttar Pradesh in Lucknow at Vikasnagar"
idx3=sentence.index("in")#return index where first searched string end
print (f"in is found at index {idx3}")

sen="zen zeen "
idx4=sen.index(" zeen ")#space, return where first searched string starts
print(idx4)

start_idx=(0)
for i in range(5):
    idx6=data.find("in",start_idx)#start finding from the given index
    print(f"in is found at {idx6}")
    start_idx=idx6+1
num_of_in=data.count("in")#count the number of times a certain word has occured in a string
print(f"in occurs {num_of_in} times")    

str="this is my house is "
start_idx=(0)
for i in range(5):
    idx6=str.find("is",start_idx)#start finding from the given index
    print(f"is was found at {idx6}")
    start_idx=idx6+1
num_of_in=str.count("is")#count the number of times a certain word has occured in a string
print(f"is occurs {num_of_in} times")    




