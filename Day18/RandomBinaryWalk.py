import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return r,g,b
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
walk=True
while walk==True:
  i = random.randint(0,2)

  tim.pensize(10)
  if i ==0:
    tim.right(45)
    tim.forward(10)
    tim.color(random_color())
  elif i==1:
    tim.color(random_color())
    tim.left(45)
    tim.forward(10)
