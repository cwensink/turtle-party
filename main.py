#Turtle Party Project
#by Chris Wensink
# 2/1/2024

#5 hour mini course by Joy of Coding by Emily Hill

#Day 1
print("Hello, World!")

#Simple Blue triangle example
import turtle

#turtle.color("green")
def triangle(size):
  for i in range(3):
    turtle.color("red")
    turtle.forward(size)
    turtle.right(120)

#for i in range(6):
#  turtle.left(60)
#  triangle(50,120)
#  triangle(75,120)
#  triangle(100,120)

#def hexagons():
#  for i in range(6):
#    turtle.right(60)
#    triangle(50,120)
#    triangle(75,120)
#    triangle(100,120)
    
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def forward(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()

#triangle(100)
#back(75)
#triangle(50)
#back(50)
#triangle(25)

def square(size):
  for i in range(4):
    turtle.color("red")
    turtle.forward(size)
    turtle.right(90)

def newline():
  turtle.penup()
  turtle.right(90)
  turtle.forward(len)
  turtle.left(90)
  turtle.forward(len)
  turtle.pendown()

def spiral(length, angle):
  for i in range(4):
   turtle.forward(length)
   turtle.right(angle)  
   turtle.forward(length + 5)
   
#spiral(25,90)
#newline()
##square(100)
#back(75)
#square(50)
#back(50)
#square(25)

#turtle.color("green") 
#hexagons()
#turtle.left(5)
#turtle.color("red")
#turtle.left(5)
#hexagons()
#turtle.color("blue")
#turtle.left(5)
#hexagons()

#turtle.forward(size)
#turtle.right(turn)
#turtle.forward(size)
#turtle.right(turn)

#def square(size):
#  for i in range(4):
#    turtle.forward(size)
#    turtle.right(90)
    
#square(50)
#turtle.penup
#turtle.back(100)
#square(25)

#turtle.back(100)
#def row(count):
#  for i in range(count):
#     square(20)
#     turtle.forward(20)
     
#def grid(count):
#  for i in range(count):
#    row(8)
#    turtle.back(160)
#    #turtle.right(90)
#    turtle.penup
#    turtle.right(90)
#    turtle.left(90)
    
    
#grid(2)
square(100)
back(125)
square(50)
#row(8)

#Turtle party - putting it all together
#what's next
#keep conversation going on facebook group facebook.com/groups/joy.of.coding
#Follow facebook.com/joyofcoding4all page
#subscribe to joy of coding youtube channel
def polygon(sides,length):
  angle = (360/sides)
  if sides < 3:
    print("You must have at least 3 sides, now exiting")
    quit()
  else:
    if sides == 3:
      print("triangle")
    if sides == 4:
      print("square")
    if sides == 5:
      print("pentagon")
    if sides == 6:
      print("hexagon")
    if sides == 7:
      print("heptagon")
    if sides == 8:
      print("octagon")
    if sides == 9:
      print("nonagon")
    if sides == 10:
      print("decagon")
    if sides == 11:
      print("hendecagon")
    if sides == 12:
      print("dodecagon")
      
  for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)
  #Write test to ensure sides are less than 3, then exit
  
  #get number of sides, then divide that by 360 degrees to complete the shape
  #i.e. triangle, 3 sides, 120 degrees, square 4 sides 90 degrees pentagon 5 sides 72
sides = 3
length = 50
angle = (360/sides)
#for i in range(9):
#  polygon(sides,length)
#  sides +=1
#  turtle.forward(length)
#  turtle.left(angle)
  #turtle.left(angle)
#  polygon(sides,length)
#  turtle.forward(length)
#  turtle.left(angle)
#  turtle.color
#sides=3
#polygon(sides,50)
#back(len)
#polygon(sides+1,25)
#back(len)
#polygon(sides+2,15)





#    print("You must have a minimum of 3 sides")
#    exit

  
