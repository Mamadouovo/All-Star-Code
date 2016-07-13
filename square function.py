from Myro import *
init("sim")
def square():
    i=0
    while i<4:
        turnBy(90)
        forward(1,1)
        i=i+1
square()