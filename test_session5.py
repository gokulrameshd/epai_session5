import pytest
import inspect
from test_utils import *
import random
import re
import numpy as np
import time
import session5
from session5 import *
from math import tan , pi 



def test_function_names():
    assert function_name_had_cap_letter(session5) == False, "One of your function has a capitalized alphabet!"


# def test_print_1():
#     assert time_it(print_1, 1, 2, 3, repetitions=5, sep='-', end= ' ***\n') == ['1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n'] , "print is fine"
#     # assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"

def test_print_1_1():
    assert print_1(args = (1, 2, 3)  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == '1-2-3 ***\n' , "print_1 function is working!!!"

def test_print_1_2():
    assert print_1(args = ('a', 's', 'd')  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == 'a-s-d ***\n' , "print_1 function is working!!!"

def test_print_1_3():
    assert print_1(args = (3, 4, 5)  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == '3-4-5 ***\n' , "print_1 function is working!!!"

def test_print_1_4():
    assert print_1(args = ('asd', 'fgh', 'jkl')  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == 'asd-fgh-jkl ***\n' , "print_1 function is working!!!"

def test_print_1_5():
    assert print_1(args = (123, 234, 345)  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == '123-234-345 ***\n' , "print_1 function is working!!!"

def test_squared_power_list_1():
    assert squared_power_list(args= (2,) , kwargs = {'start':0, 'end':5} ) == [1, 2, 4, 8, 16,32], 'squared_power_list function works!!!'

def test_squared_power_list_2():
    with pytest.raises(ValueError) as e_info:
        r = session5.squared_power_list(args= (2,) , kwargs = {'start':-1, 'end':5} )
    # assert squared_power_list(args= (2,) , kwargs = {'start':-1, 'end':5} ) == [1, 2, 4, 8, 16], 'squared_power_list function works!!!'

def test_squared_power_list_3():
    with pytest.raises(ValueError) as e_info:
        r = session5.squared_power_list(args= (2,) , kwargs = {'start':0, 'end':-5} )

def test_polygon_area_1():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(args= (0,) , kwargs = {'sides':4} ) 

def test_polygon_area_2():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(args= (5,) , kwargs = {'sides':2} ) 

def test_polygon_area_3():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(args= (0,) , kwargs = {'sides':2} ) 

def test_polygon_area_4():
    assert session5.polygon_area(args= (4,) , kwargs = {'sides':4} ) == 16 , 'polygon area function is working'

def test_temp_converter_1():
    assert session5.temp_converter(args=(0,),kwargs = {'temp_given_in' : 'f'}) == -18 , 'temp_converter perfectly working!!'

def test_temp_converter_2():
    assert session5.temp_converter(args=(100,),kwargs = {'temp_given_in' : 'f'}) == 38 , 'temp_converter perfectly working!!'


def test_temp_converter_3():
    assert session5.temp_converter(args=(-100,),kwargs = {'temp_given_in' : 'k'}) == -373 , 'temp_converter perfectly working!!'


def test_speed_converter_1():
    assert speed_converter(args = (100,), kwargs = {'dist':'m', 'time':'s'}) == 27.777755555573332 ,'speed_converter_1 perfectly working!!'

def test_speed_converter_2():
    assert speed_converter(args = (100,), kwargs = {'dist':'ft', 'time':'s'}) == 91.1388159778361 ,'speed_converter_1 perfectly working!!'

def test_speed_converter_3():
    assert speed_converter(args = (100,), kwargs = {'dist':'ft', 'time':'s'}) == 91.1388159778361 ,'speed_converter_1 perfectly working!!'


# time_it(print_1, 1, 2, 3, repetitions=5, sep='-', end= ' ***\n')
# time_it(squared_power_list, 2, start=0, end=5, repetitons=5)
# time_it(polygon_area, 4, sides = 4, repetitons=10)
# time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
# time_it(speed_converter, 100, dist='m', time='s', repetitons=200)

def test_print_time_it():
    ret , time = time_it(print_1, 1, 2, 3, repetitions=5, sep='-', end= ' ***\n')
    assert ret == ['1-2-3 ***\n','1-2-3 ***\n','1-2-3 ***\n','1-2-3 ***\n','1-2-3 ***\n'] , 'worked!!'
    assert time != None , 'worked!!'

def test_squared_power_list_time_it():
    ret , time = time_it(squared_power_list, 2, start=0, end=5, repetitions =5)
    assert ret == [[1,2,4,8,16,32],[1,2,4,8,16,32],[1,2,4,8,16,32],[1,2,4,8,16,32],[1,2,4,8,16,32]] , 'worked!!'
    assert len(ret) == 5 , "Worked!!"
    # assert time > , 'worked!!'

def test_polygon_area__time_it():
    ret , time = time_it(polygon_area, 4, sides = 4, repetitions=10)
    assert ret == [16,16,16,16,16,16,16,16,16,16] , 'worked!!'

def test_temp_converter_time_it():
    ret , time = time_it(temp_converter, 100, temp_given_in = 'f', repetitions = 100)
    assert len(ret) == 100, "worked!!"

def test_speed_converter_time_it():
    ret , time =  time_it(speed_converter, 100, dist='m', time='s', repetitions=200)
    assert len(ret) == 200, "worked!!"

def test_speed_converter_time_it_1():
    ret , time =  time_it(speed_converter, 10, dist='m', time='s', repetitions=200)
    assert ret[1] == 2.777775555557333, "worked!!"
