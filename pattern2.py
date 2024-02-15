from turtle import*
speed(0)

def polygon(side):
    for _ in range(side):
        fd(100)
        lt(360/side)
# tesing the function
for _ in range(6):
    polygon(10)
    polygon(6)
    polygon(4)
    lt(60)
hideturtle()
mainloop()