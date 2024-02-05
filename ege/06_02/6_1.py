import turtle as t


t.tracer(False)
k = 35
for i in range(7):
    t.forward(10 * k)
    t.right(120)
t.penup()
for x in range(-30, 10):
    for y in range(-30, 10):
        t.goto(x * k, y * k)
        t.dot()
t.exitonclick()
