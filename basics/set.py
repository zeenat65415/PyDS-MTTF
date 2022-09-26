#set is an unordered collection of data.
#duplicate values are eliminated by set
#set itself is mutable.but we can insert only immutable data in set like we can keep imuutable data string,tuple,numerical values.
my_set={1,2,3,4,3,2}
print(my_set)

my_set=set([1,2,3,2])
print(my_set)

#my_set={1,2,[3,4]}#unhashable type"list

a=set()#to create empty set

my_set={1,3}
print(my_set)

my_set.add(2)#adds only one item at a time
print(my_set)

my_set.update([2,3,4])#add or update multiple items at a time
print(my_set)

my_set.update[[4,5],[1,6,8]]
print(my_set)

#removing items from set
my_set={1,2,3,4,5,6}
print(my_set)

my_set.discard(4)
print(my_set)

my_set.remove(6)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

