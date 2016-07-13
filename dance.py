from Myro import *
init("sim")
i=0

while i<5:
    forward(4,1)
    backward(4,1)
    turnLeft(4,1)
    forward(4,1)
    backward(4,1)
    turnRight(4,1)
    forward(4,1)
    backward(4,1)
    i=i+1

    
j = 0
while j <500:
    rotate(10)
    print(j)
    j = j+1
  
stop ()
  
