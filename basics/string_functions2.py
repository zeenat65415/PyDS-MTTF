#utility functions: find,count,split,replace,join
msg="we will be seeing the horizon"


words=msg.split()
print(words)# creates a list by splitting the given string into word.

words=msg.split('e')
print(words)

#replace()
updated_msg=msg.replace('seeing',"viewing")
print(updated_msg)

updated_msg=msg.replace("e","")
print(updated_msg)

#join()
path=["users","mypc","documents","data","file.txt"]#is used to join together the elements of the list.
content= "/".join(path)
print(content)

#strip()#used mostly during form validation is used to remove extra spaces but not remove space between words
name="  Hello  Steve   "
cleaned_name=name.strip() 
print(cleaned_name)
print(len(name),len(cleaned_name))

msg2='''

we are venom

'''
cleaned_msg2=msg2.strip()
print(cleaned_msg2)
print(len(msg2),len(cleaned_msg2))

msg3=name.replace(" ","")
print(msg3)


from helper import read#done in count_all_alphabets.py
data=read('pride_n_prejudice.txt')
#wap to find frequency of all the vowels in the 'data'

for vowel in'aeiou':
  print(f"{vowel}=>{data.lower().count(vowel)} times")
for vowel in'AEIOU':
  print(f"{vowel}=>{data.upper().count(vowel)} times")

#wap to remove all the punctuations from the string
str='he@#ll%o!@ &*(!@wo!@rl!d)'
from string import punctuation
for p in punctuation:
    str=str.replace(p,"")
print(str)    

