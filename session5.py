import numpy as np
import time
from math import tan , pi 

def time_it(func_1 , *args ,  repetitions = 6 , **kwargs ):
#     start_time = time.time()
    # print("args:", args)
    # print("kwargs:",kwargs)
    t = []
    r = []
    for i in range(repetitions):
        start_time = time.time()
        ret = func_1(args ,kwargs )
        # print(ret)
        end_time = time.time()
        t.append(end_time - start_time)
        r.append(ret)
    avg_time = (np.mean(t))
    # print(f'Time taken to ececute the given function {repetitions} times = {(t/repetitions)}, seconds')	
    return r,avg_time


def print_1(args  ,kwargs):
    a = ""
    sep  = kwargs['sep']
    end = kwargs['end']
    for i ,j in enumerate(args) :
        if i < len(args)-1:
            a += str(j)+sep
        else:
            a += str(j)
    a = a+str(end)
#     a = 1
#     print(a)
    return a

def squared_power_list(args, kwargs ):
    n = args[0]
    start =  kwargs['start']
    end = kwargs['end']
    if start <0  or end < 0:
        raise ValueError("Input value should be greater than zero ")
    lis = []
    for i in range(start, end+1):
        a = n**i
        lis.append(a)
    return lis
    

def polygon_area(args,kwargs):
    length = args[0]
    if length <= 0:
        raise ValueError("Input length value should be greater than zero ")
    sides = kwargs['sides']
    if sides < 3:
        raise ValueError("Number of sides should be greater than two.")
    area = round(sides * length**2 )/(4 *tan(pi/sides))
    return (int(area))


def temp_converter(args , kwargs):
    t = args[0]
    temp_given_in = kwargs['temp_given_in']
    if temp_given_in == "f":
        c = ((t - 32) * (5/9))
    elif temp_given_in == "k":
        c = t - 273.15
    else :
        raise ValueError("The input should be kelvin or farenheit ")
    return (round(c))


def speed_converter(args , kwargs):
    kmph = args[0]
    dist = kwargs['dist']
    time = kwargs['time']
    
    if kmph < 0:
        raise ValueError("Input kmph value should not be less than zero ")
    if dist not in ['km' , 'm' , 'ft','yrd']:
        raise ValueError("Enter proper metric ")
    if time not in ['ms' , 's' , 'min','hr','day']:
        raise ValueError("Enter proper metric ")

    if dist is 'km':
        d = kmph
    if dist is 'm':
        d = kmph * 1000
    if dist is 'ft':
        d = kmph * 3281
    if dist is 'yrd':
        d = kmph * 1093.61
        
    if time is 'ms':
        t = 3600002.88
    if  time is 's':
        t = 3600.00288
    if time is 'min':
        t =  60
    if time is 'hr':
        t = time
    if time is 'day':
        t = 0.0416667# ms/s/m/hr/day
        
    speed = float(d)/float(t)
    
    return speed
