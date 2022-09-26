import helper as h # in helper file read function was used
from string import punctuation

data = h.read("basics/pride_n_prejudice.txt")
print(len(data))

#remove punctuation
for p in punctuation:
    data=data.replace(p,"")
 

#split into words and remove spaces and empty strings
words=[word.strip() for word in data.lower().split()]#data ko lower case mai convert karke we will split

print("TOTAL WORDS FOUND :",len(words))
print("UNIQUE WORDS FOUND:",len(set(words)))

#create a dictionary(word count)# sorting on the basis of word occurence
# wc= {}
# for word in set(words):
#     wc[word] = words.count(word)
#or
wc={}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1        

# #first 50 words
# for k,v in list(wc.items())[:50]:
#     print (k,v)

#sorting a dictionary-> wc.items() returns a list of tuples
wc = sorted(wc.items(),key=lambda x: x[1], reverse=True)# reverse=True means we are sorting in ascending order


# print the top 10 words
for i in range(10):
    print(wc[i])

# #word cloud
# from wordcloud import wordcloud
# import matplotlib.pylot as plt

