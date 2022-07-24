# using range() and for loop
from turtle import*

speed=('slowest')

sides=10
for i in range(sides):
    forward(100)
    left(360/sides)

mainloop()    
