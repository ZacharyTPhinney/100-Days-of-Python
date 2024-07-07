import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
walk=True
while walk==True:
  i = random.randint(0,2)

  for j in range(0,100):
    if i ==0:
      tim.right(j)
      tim.forward(50)
      tim.color(random.choice(colours))
    elif i==1:
      tim.color(random.choice(colours))
      tim.left(j)
      tim.forward(10)