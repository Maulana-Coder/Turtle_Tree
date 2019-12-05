import turtle as tu

wn = tu.Screen()
wn.title("Tree - Maulana ID")
wn.bgcolor("black")

fac = tu.Turtle()
fac.setposition(0, -150)
fac.color("lime")
fac.left(90)
fac.speed(15)
fac.hideturtle()

def draw(l):
    if (l < 10):
        return
    else:
        fac.forward(l)
        fac.left(30)
        draw(3*l/4)
        fac.right(60)
        draw(3*l/4)
        fac.left(30)
        fac.backward(l)      
draw(100)

def credits():
    tu.color("white")
    tu.speed(0)
    tu.penup()
    tu.setpos(-40, -250)
    tu.write("   Created\nBy Maulana ID", font=("Consolas", 10, "bold",))
    tu.penup()
    tu.hideturtle()
credits()
