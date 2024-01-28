import pgzrun
import asyncio
from random import randint
import time

HEIGHT = 400
WIDTH = 500

x = WIDTH
y = HEIGHT
coins = 0
current_level = 1
game_under = False
game_over = False
z = False
b = 0

fox = Actor("fox")
fox.pos = 250, 360

heart = Actor("heart")

heart.pos = randint(1,400), 360

heart2 = Actor("heart")
heart2.pos = randint(1,400), 360

heart3 = Actor("heart")
heart3.pos = randint(1,400), 360

heart4 = Actor("heart")
heart4.pos = randint(1,400), 360

lightning = Actor("lightning")
lightning.pos = 500,500

def draw():
    global b
    global coins
    global current_level
    if coins < 0:
        screen.fill("blue")
        screen.draw.text("Game over - You got to level " + str(current_level), color = "red", topleft = (10, 10))
    elif coins > 10:
        coins = 0
        fox.pos = 250, 360
        heart.pos = 0,randint(1,200)
        heart2.pos = 0,randint(1,200)
        heart3.pos = 0,randint(1,200)
        heart4.pos = 0,randint(1,200)
        current_level = current_level + 1
    else:
        screen.fill("black")
        fox.draw()
        heart.draw()
        heart2.draw()
        heart3.draw()
        heart4.draw()
        lightning.draw()
        heart.x = heart.x + current_level + 2
        heart2.x = heart2.x + current_level + 2
        heart3.x = heart3.x + current_level + 2
        heart4.x = heart4.x + current_level + 2
        screen.draw.text("Coins:" + str(coins), color = "red", topleft = (10, 10))
        screen.draw.text("Level:" + str(current_level), color = "red", topright = (450, 350))

    #if game_over:
        #screen.fill("red")
        #screen.draw.text("You won!", topleft = (10,10), fontsize = 60)
        #fox.pos = 250, 360
        #heart.pos = randint(1,200), 360
        #heart2.pos = randint(1,200), 360
        #heart3.pos = randint(1,200), 360
        #heart4.pos = randint(1,200), 360
        #time.sleep(5)
def offscreen():
    global coins
    if heart.x > 500:
       heart.pos = randint(1,200), randint(20,360)
       coins = coins - randint(1,2)
    if heart2.x > 500:
       heart2.pos = randint(1,200), randint(20,360)
       coins = coins - randint(1,2)
    if heart3.x > 500:
       heart3.pos = randint(1,200), randint(20,360)
       coins = coins - randint(1,2)
    if heart4.x > 500:
       heart4.pos = randint(1,200), randint(20,360)
       coins = coins - randint(1,2)

def keyboardcheck():
    global game_over
    if keyboard.up:
        move = fox.y - 15
        fox.y = move
        move2 = 360
        animate(fox, duration = 0.5, on_finished = None, y = move)
        animate(fox , duration = 1, on_finished = None, y = move2)
    if keyboard.left:
        left = fox.x - 30
        animate(fox, duration = 0.2, on_finished = None, x = left)
    elif keyboard.right:
        right = fox.x + 30
        animate(fox, duration = 0.2, on_finished = None, x = right)

    if lightning.colliderect(fox):
        z = True
        if randint(1,50) == 1:
            z = False

def check():
    global game_over
    global b
    global game_under
    
    if coins < 0:
        game_under = True

        screen.draw.text("You lost", topleft = (10,10), fontsize = 60)
    if coins > 19:
        game_over = True
        
def update():
    global coins
    global game_over
    global lightning
    keyboardcheck()
    offscreen()
    check()
    if fox.colliderect(heart):
        if z == True:
            coins = coins + 1
        else:
            coins = coins + 2
        heart.x = 0
        heart.y = randint(20,360)
    if fox.colliderect(heart2):
        if z == False:
            coins = coins + 1
        else:
            coins = coins + 2
        heart2.x = 0
        heart2.y = randint(20,360)
    if fox.colliderect(heart3):
        if z == False:
            coins = coins + 1
        else:
            coins = coins + 2
        heart3.x = 0
        heart3.y = randint(20,360)
    if fox.colliderect(heart4):
        if z != True:
            coins = coins + 1
        else:
            coins = coins + 2
        heart4.x = 0
        heart4.y = randint(20,360)
    
    if randint(1,100) == 1:
        lightning.pos = 0,0
        animate(lightning, duration = 1, on_finished = None, x = randint(1, 500), y = 400) 

async def main():
    pgzrun.go()
    await asyncio.sleep(0)

asyncio.run(main())




        
