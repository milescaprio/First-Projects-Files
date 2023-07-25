import turtle
t = turtle.Pen()
turtle.bgcolor("blue")
colors=["red","orange","yellow","green","purple"]
for s in range(5):
    t.pencolor(colors[s%5])
    t.forward(350)
    t.left(144)
