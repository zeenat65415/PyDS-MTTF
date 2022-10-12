#set is an unordered collection of data.
#duplicate values are eliminated by set
#set itself is mutable.but we can insert only immutable data in set like we can keep immutable data like  string,tuple,numerical values.

#sets cannot have duplicates
#Output:{1,2,3,4}
my_set={1,2,3,4,3,2}
print(my_set)


#set of mixed datatypes
my_set={1.0,"Oye",(1,2,3)}
print(my_set)



#ex1- my_set={1,2,[3,4]}#unhashable type"list
#or ex2-
# my__set={[1,2,3]}#TypeError:unhashable type: 'list'
# print(my_set)
#therefore sets cannot have mutable items like List.This will cause an error.
#but we can make a set from a list
list=[1,2,3,4,8,9,10]
my_set=set(list)
print(my_set)
#or
my_set=set([1,2,'Apple'])
print(my_set)

a=set()#to create empty set(initialize a with set())
print(type(a)) # <class 'set'>

## Modifying a set
##Sets are mutable.However since they are unordered ,indexing has no meaning.

#initialize my_set
my_set={1,3}
print(my_set)

#add an element
#Output:{1,2,3}
# my_set.add(2,3)#adds only one item at a time
# print(my_set)#TypeError: set.add() takes exactly one argument (2 given)
my_set.add(2)
print(my_set)

my_set.update([2,3,4])# update fn add multiple items at a time
print(my_set)#{1,2,3,4}

#add list and set
my_set.update([4,5],{1,6,8})
print(my_set)#{1,2,3,4,5,6,8}
print(type(my_set))


##Removing items from set
##A particular item can be removed from a set using the methods discard() and remove() 
my_set={1,2,3,4,5,6}
print(my_set)

#discard an element
# my_set.discard(4,5)
# print(my_set) #TypeError: set.discard() takes exactly one argument (2 given)
my_set.discard(4)
print(my_set)

#remove an element
my_set.remove(6)
print(my_set)#IF WE GIVE MORE THAN TWO ARGUEMENTS IT WILL ALSO GIVE ERRORT.ypeError: setremove() takes exactly one argument (2 given)
#therefore discard and remove are same.

#pops a random item
my_set.pop()
print(my_set)

#clear my_set
#Output: set()
my_set.clear()
print(my_set)

