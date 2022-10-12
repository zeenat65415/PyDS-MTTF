import helper as h # in helper.py file read function was used
from string import punctuation#(variable) punctuation: LiteralString  and  h,helperandstring are  module

data=h.read("basics/pride_n_prejudice.txt")
print(len(data))#782454

# remove punctuation00
for p in punctuation:
    data=data.replace(p,"")

#split into words and remove spaces and empty strings
words=[word.strip() for word in data.lower().split()]#data ko lower case mai convert karke we will split

print("TOTAL WORDS FOUND: ", len(words))#124740,len return of items in a container
print("UNIQUE WORDS FOUND: ", len(set(words)))#8138 #(class) set,builds an unorderd collection of unique elements

#create a dictionary
# wc = {}     #wc- is a dictionary          
# for word in set(words):
#     wc[word]=words.count(word)# count-Return number of occurrences of value.
#or
wc={}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1        

#first 50 words
# for k,v in list(wc.items())[:50]:
#     print(k,v)

# sorting the dictionary(on the basis of word occurence) -> wc.items() returns a list of tuples[()]
wc = sorted(wc.items(), key=lambda x: x[1], reverse=True) #wc becomes a list of tuple earlier it was a dictionary.
# reverse=True means we are sorting in ascending order
#items -is a method .D.items() -> a set-like object providing a view on D's items

# print top 10 words
for i in range(10):
    print(wc[i])#(variable) wc: list[tuple]

# #word cloud
# from wordcloud import WordCloud
# import matplotlib.pyPlot as plt

# #create a string with all the words
#text =" ".join(words)
