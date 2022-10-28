from random import randint as ri
import pgzrun

WIDTH = 800
HEIGHT = 400

# all the class logic
class Player(Actor):
    #override the default constructor
    def _init_(self,image,speed=5):
        pos = ri(0,WIDTH), ri(0,HEIGHT) # generate a random x,y coordinate
        super()._init_(image,pos) # call the random class constructor and pass image and pos
        self.speed = speed # add a new instance variable

    def move(self):
        if keyboard.W:
            self.y -= self.speed
        if  keyboard.S:
            self.y += self.speed
        if keyboard.A:
            self.x -= self.speed
            self.angle = +10
        if keyboard.D:
            self.x += self.speed   
            self.angle =  -10 
        else:
            self.angle = 0

    def check_boundary(self):
       if self.x < 0: #agar player left side se bahar  ja raha hai
          self.x = WIDTH  #toh right side pe dikhne lage
       if self.x > WIDTH: # vice versa
          self.x = 0
       if self.y < 0:
          self.y = HEIGHT
       if self.y > HEIGHT:
          self.y = 0

# main game code
p = Player("ironman")
def draw(): 
    screen.fill("black")
    screen.blit("bg4" ,(0,0))
    p.draw()  
def update():
    p.move()
    p.check_boundary()
pgzrun.go()
