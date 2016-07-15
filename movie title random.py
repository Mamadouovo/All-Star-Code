from random import *
list1 = ["Return","Big","Small","Sharp","Fast","Super","Man","Attack","Appocalypse","Scary"]
list2 = ["The","Bang","Of","Amazing","2","Boy","Girl","Fly","Speed","Furious"]
list3 = ["Plane","Fall","Jump","Hard","Fire","Tornado","Disaster","Natural","Tsunami","Rise"]
i = 0 
while i <= 10:
    x = list1[randrange(10)]
    y = list2[randrange(10)]
    z = list3[randrange(10)]
    title = x +" "+ y +" "+ z
    print(title)

    

    i=i+1
    #print(title)
    