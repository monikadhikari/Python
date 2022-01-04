## Library import 
import turtle


## num to maintain mirror the first draw
def draw(num):
  tommy.forward(100*num)
  tommy.penup()
  tommy.goto(0,-100)
  tommy.pendown()
  tommy.forward(100*num)
  tommy.goto(100*num,-150)
  tommy.goto(150*num,-50)
  tommy.goto(100*num,50)
  tommy.goto(100*num,0)
  tommy.goto(100*num,0)
  tommy.goto(0,0)

#Creating Canvas  
canvas=turtle.Screen()
tommy = turtle.Turtle()

##Calling draw Funtion
draw(1)
draw(-1)
