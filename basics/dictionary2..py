from pprint import pp 

movies={}
movies["Top Gun: Maverick"]=8.3
movies["Everything Everywhere All at Once"]=8.1
movies["Spider_Man: No Way Home"]=8.2

print(movies)
pp(movies)

print("only keys =>")
for item in movies:
 print(item)    

print("only values =>")
for item in movies:#(variable) movies: dict
    print(movies[item])#(variable) item: Any

print("both key and values =>")
for key in movies:
    print(key, movies[key])

print("using dict.items() method =>")
for k,v in movies.items():#D.items() -> a set-like object providing a view on D's items,where items() is a method.
      print(k, v)  


#user input
for i in range(3):
    name=input("Movie Name:")
    rating=float(input("Movie Rating: "))
    movies[name]=rating
#The Godfather,Inception,Joker

print("using dict.items() method")
for k,v in movies.items():
    print(k,v)                