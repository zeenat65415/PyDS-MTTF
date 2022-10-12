import pgzrun

WIDTG=800
HEIGHT=400

class Player(Actor):
    #o verride the defaut constructor
    def _init_(self,image,speed=5):
        pos = ri(0,WIDTY),ri(0,HEIGHT)# generate a random x,y coordinate
        super()._init_(image,pos)#call the parent class constructor and pass image andd                                                                                                