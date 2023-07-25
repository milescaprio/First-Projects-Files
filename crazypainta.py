import turtle
import random
turtle.speed(0)
playman = 56
t = turtle.Pen()
colors = ["blue","DarkBlue","royal blue","red","pink","dark red","powder blue","pale violet red","peach puff","orange red","dark orange","LightBlue","lime green","magenta","light yellow","light steel blue","maroon","yellow green","white","tomato","thistle","green","sea green","rosy brown","brown","saddle brown","seashell","sienna","papaya whip","indigo"]
turtle.bgcolor("black")
while playman == 56:
    x = random.randrange(-960,960)
    y = random.randrange(-800,800)
    t.pencolor(random.choice(colors))
    t.setpos(x,y)
    playman = 56
    
          
