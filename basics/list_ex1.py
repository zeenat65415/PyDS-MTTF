#list are mutable,we can change.

movies=['Sholay','Baghban','DDLJ',
'Ironman','RRR','Inception','Spiderman',
'Kung Fu Panda','Suryavansham','Batman']

print(len(movies))
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('All movies except first 3',movies[3:])
print('movies with even indexes',movies[::2])