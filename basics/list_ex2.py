books=['Steelheart','Firefight','Osmosis','Calamity']

books.append('The Final Empire')
books.append('Atomic Habit')
books.append('You can win')
books.append('Three mistakes of my life')#adding more than 2 items at a time will give error
print(books)

print('idx\t| book')# 4 sapce gap
for i,b in enumerate(books):
    print(f'{i}\t| {b}')


# list are mutable you can change name of all elements of list

books[6]='The Well of Ascension'# update
books[-1]='The Hero of Ages'
books[2]='Legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}' )


books.insert(3,'Legion: Skin deep')
books.insert(5,'Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('Steelheart')
books.remove('Legion')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

#Extend function-
fruits=['apple','Banana','Cherry','Guava']
dry_fruits=['Almond','Cashew','Walnut']
fruits.extend(dry_fruits)
print(fruits)

#sorting does not work on mixed datatypes
#removes remove one list a time

