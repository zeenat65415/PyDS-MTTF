#there are 11 functions in list
#tuple have two function
# 1
x=(1,2,3,1,2,3,1,2,3,1,1,1,2,3,3,3,3,1,1,1)

print('3 occurs =>',x.count(3))
print('5 occurs =>',x.count(5))
print('1 occurs =>',x.count(1))

y=(12,45,556,89,32,32,12,45,55,21,556)
print("556 found at =>",y.index(556))#find first index whwere 556 was found.
print("32 found at =>",y.index(32))
print("12 found at =>",y.index(12))
print("12 found at =>",y.index(12,1))#return index where 12 was found after index-0
print("556 found at =>",y.index(556,3))##return index where 12 was found after index-2
# 2
my_tuple=('a','p','p','l','e')
print("p occurs =>",my_tuple.count('p'),"times") #Output: 2
print("l found at index =>",my_tuple.index('l')) #Output: 3