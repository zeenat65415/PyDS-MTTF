from turtle import*

speed('fastest')
bgcolor('black')
pencolor('red')

for i in range(97):
    forward(i)
    left(90)
    dot(i)

mainloop()    