from pprint import pp 

movies={}
movies["Top Gun:Maverick"]=8.3
movies["Everything Everywhere All at Once"]=8.1
movies["Spider_Man:No Way Home"]=8.2
#pp(movies)

for item in movies:
    print(movies)

print("only values")
for item in movies:
    print(movies[item])

print("both key and values")
for key in movies:
    print(key, movies[key])

print("using dict.items() method")
for k,v in movies.item():
      print(k, v)  


#user input
for i in range(3):
    name=input("Movie Name:")
    rating=float(input("Movie Rating: "))
    movies[name]=rating

print("using dict.items() method")
for k,v in movies.item():
    print(k,v)                