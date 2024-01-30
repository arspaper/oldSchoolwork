import turtle as t


t.tracer(False)
k = 35
for i in range(8):
    t.right(45 * k)
    t.forward(8 * k)
t.penup()
for x in range(-30, 10):
    for y in range(-30, 10):
        t.goto(x * k, y*k)
        t.dot()
t.exitonclick()
