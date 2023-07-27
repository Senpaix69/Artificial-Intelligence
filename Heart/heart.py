import turtle
pen = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Message From Senpai")

def curve():
	for i in range(100):
		pen.right(2)
		pen.forward(2)
def heart():
	pen.fillcolor('red')
	pen.begin_fill()
	pen.left(140)
	pen.forward(113)
	curve()
	pen.left(120)
	curve()
	pen.forward(112)
	pen.end_fill()

def txt():
	pen.up()
	pen.setpos(-48, 95)
	pen.down()
	pen.color('white')
	pen.write("I Love You", font=(
	"Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()
turtle.done()