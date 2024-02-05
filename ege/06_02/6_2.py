import turtle as t


t.tracer(False)
k = 15

for i in range(2):
    t.forward(8 * k)
    t.right(90)
    t.forward(18 * k)
    t.right(90)

t.penup()

t.forward(4 * k)
t.right(90)
t.forward(10 * k)
t.left(90)

t.pendown()
t.color("red")
for i in range(2):
    t.forward(17 * k)
    t.right(90)
    t.forward(7 * k)
    t.right(90)

t.penup()

t.color("black")
for x in range(-30, 40):
    for y in range(-30, 40):
        t.goto(x * k, y * k)
        t.dot()
t.exitonclick()
