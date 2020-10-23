import time 
import os



def measure_time(func):
    t_zero=time.process_time()
    
    t_total=time.process_time()-t_zero
    
    return func,t_total

def add(a,b):
    return a+b




func,time=measure_time(add(3,6))
print("Total execution time of the given function is {}".format(time))
