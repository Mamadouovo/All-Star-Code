from Myro import *
init("sim")
penDown()
speed=int(input("what is the speed?"))
second=int(input("what is the second?"))
def square():
    penDown("red")
    forward(speed, second)
    turnBy(90)
    forward(speed, second)
    turnBy(90)
    forward(speed, second)
    turnBy(90)
    forward(speed, second)
    turnBy(90)
    forward(speed, second)
    penUp()
    forward(1, 1)
square()
i=0
while i<4:
    square()
    i=i+1

