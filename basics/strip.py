# strip is a mehod:Return a copy of the string with leading and trailing whitespace removed.
# If chars is given and not None, remove characters in chars instead.

word = "    hello    world "
print("before strip =>",word)
print("after strip =>",word.strip())

word1="hello"
print("before strip =>",word1)
print("after strip =>",word1.strip())

#split
word=" Hii!!  , how are you?"
print("before split =>",word)
print("after split =>",word.split())
print("after split =>",word.split(","))
#print("after split =>",word.split(""))#ValueError: empty separator
print("after split =>",word.split(",",0))
print("after split =>",word.split(",",3))
print("after split =>",word.split(",",4))

#to remove punctuation marks
str="hell@@123::are you ok??"
from string import punctuation
for m in punctuation:
    str=str.replace(m,"")
print(str)    