import turtle
wn = turtle.Screen()         # Set up the window and its attributes

hailey = turtle.Pen()
hailey.shape("turtle")

hailey.forward(100)
hailey.left(90)
hailey.forward(100)
hailey.left(90)
hailey.forward(100)
hailey.left(90)
hailey.forward(100)
hailey.reset()
hailey.color("blue")
hailey.forward(100)
hailey.circle(100)
hailey.circle(-100)
hailey.reset()

hailey.color("red")
hailey.forward(100)
hailey.up()
hailey.forward(100)
hailey.down()
hailey.circle(50)
hailey.forward(100)
hailey.width(5)
hailey.backward(200)

hailey.color("blue")
hailey.forward(200)
hailey.right(120)
hailey.forward(200)
hailey.right(120)
hailey.forward(200)
hailey.backward(100)
hailey.circle(100)
hailey.backward(10)

wn.mainloop()                # Wait for event to exit