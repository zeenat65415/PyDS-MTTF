#dictionary is an orderd collection of data.
#each itam of a dictioary has a jey and value.

#dictionary with integer keys
my_dict={1:"apple", 2:"ball"}
print(my_dict)

val=["Rajendra Singh" ,30,4,"Accounts","Staff Officer",600000,7,]#this is information which is not clear.it is not meaningful information

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
#print(val_dict["Experience"])#incorrect_KeyError

#adding a data inside dictionary
val_dict["comapany"]="Acme.inc"

print(val_dict)

from pprint import pp#another way of printing complex data like of dictionary
pp(val_dict)