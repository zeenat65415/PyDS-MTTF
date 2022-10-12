#Dictionary is an orderd collection of data.
#each itam of a dictioary has a Key and value.
#Dictionaries are optimized to retrieve the values when the key is known.
#An item has a key and a corresponding value that is expressed as a pair (key:value)

#dictionary with integer keys
my_dict={1:"apple", 2:"ball"}
print(my_dict)

val=["Rajendra Singh" ,30, 10, "Accounts", "Staff Officer", 600000, 7]#this is information which is not clear.it is not meaningful information
print(val)

val_dict={
    "employee":"Rajendra Singh","age":30,
    "experience": 10,"dept":"Accounts",
    "designation":"System Officer","salary":600000,
    "team_size":7
}

#displaying a dictionary
print(val_dict)


#we shoulld learn to retrieve and manipulate data from  dictionay
#retreival of data
ans=val_dict["designation"]#key in sqr brackets
print(ans)
print(val_dict["salary"])#correct
# print(val_dict["Experience"])#incorrect - as 'e' in experience must be in same case as during creation of vdictionary
# (KeyError: 'Experience')

#adding a data inside dictionary
val_dict["comapany"]="Acme.inc"

print(val_dict)

from pprint import pp#another way of printing complex data like of dictionary
pp(val_dict)#it displays only one key with its value in one line