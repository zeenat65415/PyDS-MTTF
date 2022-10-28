#Variable arguements

#In print() unlimited parameter can be passed
#def total(*args):#variable arguement will behave as a tuple,it also takes unlimited no of arguements
def mean(*numbers):
    print(numbers)
    print(type(numbers))

mean(1,2,3,4)


def mean(*numbers):
  if not numbers:  
      return None
  return sum(numbers)/len(numbers)

print(mean(1,2,3,4))
print(mean(1,2,3,4,5,6))
print(mean(1,22,1,1,2,3,1,321,123,1,312))
print(mean())
print(mean(10))
