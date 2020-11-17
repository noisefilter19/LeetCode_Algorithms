import random, math
rect_num=0
circle_num=0
for ind in range(1,1000000):
    x=random.uniform(0, 1)
    y=random.uniform(0, 1)
    if(math.sqrt( (x)**2 +(y)**2)<1): 
        circle_num=circle_num+1

    rect_num=rect_num+1
        
#print (rect_num/circle_num )
print (4*(circle_num/rect_num))
