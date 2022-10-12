# func1- Non parameterized and non returning functions


from random import randint

def hello(): #def is a keyword,hello is name of fn and it is non-parameterized fn
    print("HOLA")#statement
    print("AMIGOS")
    print('👋👋👋')

# # call
# hello()
# hello()
# hello()     

def roll_dice():#(function) roll_dice: () -> None
    dices = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    print(" => ",dices[randint(0,5)])
      
roll_dice()
roll_dice() 
roll_dice()
