import turtle as tle
tle.pensize(5)
tle.speed(15)
tle.bgcolor("black")
for i in range(100):
    for colours in ["yellow","blue","white","green","red","pink"]:
        tle.color(colours)
        tle.forward(200)
        tle.right(100)
        tle.forward(200)
        tle.right(100)
        tle.forward(200)
        tle.right(100)
        tle.forward(200)
        tle.right(10)
