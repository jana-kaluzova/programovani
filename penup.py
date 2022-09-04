from turtle import forward, penup, pendown, exitonclick, left, right, shape
shape ("turtle")

strana= int(input("""jak je dlouha strana a
ctverce v cm?\n"""))

for i in 0, 1, 2, 3:
    forward (strana)
    left (90)

exitonclick ()
