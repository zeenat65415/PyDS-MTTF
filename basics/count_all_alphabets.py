
from helper import read
data = read('pride_n_prejudice.txt')

from string import ascii_lowercase,ascii_uppercase#import all alphabet in lower and uppercase

for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')

#from string import ascii_uppercase
for letter in ascii_uppercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')    

# wap to find the most occuring alphabet and its frequency
freq = 0
freq_letter = ''
for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')
    if freq < counter:
        freq = counter # 70510
        freq_letter = letter # e
print(f'Most frequent letter is {freq_letter} occurs {freq} times')

#or wap to find the most occuring alphabet and its frequency
max=0
for i,n in zip(ascii_lowercase,ascii_uppercase):
    counter1=data.count(i)
    counter2=data.count(n)
    if counter1 > counter2 and counter1 >max:
        max = counter1
        alpha = i
    else:
        if counter2 > max:
            max = counter2
            alpha=n
print(f"The max occuring letter is {alpha} and it occurs {max} times")

#wap to find vowels in the given data file
for vowel in "aeiouAEIOU":
    print(f"{vowel} is found {data.count(vowel)} times")

#wap to  remove all the punctuations from the string
str="hel@rh$.!fbhhf!()jfgdhdh%#"
from string import punctuation
for marks in punctuation:
    str=str.replace(marks , '')
print(str)  