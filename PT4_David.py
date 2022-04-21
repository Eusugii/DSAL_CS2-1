#John Brent David
import turtle
import os
import math
#setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Create the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#Create the invader
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 0.2

#Create Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.hideturtle()
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)


bulletspeed = 30

#DEF bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"
#movement of the player/enemy
playerspeed = 20

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate ="fire"
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    return False

#Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")


#MAIN GAME LOOP
while True:
    
    #Move the enemy
    x = enemy.xcor()
    x+= enemyspeed
    enemy.setx(x)

    #Move the enemy back and forth
    if enemy.xcor()>280:
        y = enemy.ycor()
        y-= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor()<-280:
        y = enemy.ycor()
        y-= 40
        enemyspeed *= -1
        enemy.sety(y)

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = "ready"

    #Check for a collision 
    if isCollision(bullet,enemy):
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #Reset the enemy
        enemy.setposition(-200,250)

    if isCollision(player,enemy):
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        break