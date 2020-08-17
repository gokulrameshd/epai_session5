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


# time_it(print_1, 1, 2, 3, repitation=5, sep='-', end= ' ***\n')
# time_it(squared_power_list, 2, start=0, end=5, repetitons=5)
# time_it(polygon_area, 4, sides = 4, repetitons=10)
# time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
# time_it(speed_converter, 100, dist='m', time='s', repetitons=200)

def test_function_names():
    assert function_name_had_cap_letter(session5) == False, "One of your function has a capitalized alphabet!"


# def test_print_1():
#     assert time_it(print_1, 1, 2, 3, repitation=5, sep='-', end= ' ***\n') == ['1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n', '1-2-3 ***\n'] , "print is fine"
#     # assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"

def test_print_1():
    assert print_1(args = (1, 2, 3)  ,kwargs = {'sep' : '-', 'end' : ' ***\n'}) == '1-2-3 ***\n' , "print_1 function is working!!!"

def test_squared_power_list_1():
    assert squared_power_list(args= (2,) , kwargs = {'start':0, 'end':5} ) == [1, 2, 4, 8, 16], 'squared_power_list function works!!!'

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
    session5.polygon_area(args= (4,) , kwargs = {'sides':4} ) == 16 , 'polygon area function is working'

def test_temp_converter_1():
    session5.temp_converter(args=(0,),kwargs = {'temp_given_in' : 'f'}) == 32 , 'temp_converter perfectly working!!'

def test_temp_converter_2():
    session5.temp_converter(args=(100,),kwargs = {'temp_given_in' : 'f'}) == 212.0 , 'temp_converter perfectly working!!'


def test_temp_converter_3():
    session5.temp_converter(args=(-100,),kwargs = {'temp_given_in' : 'f'}) == -148.0 , 'temp_converter perfectly working!!'


def test_speed_converter_1():
    speed_converter(args = (100,), kwargs = {'dist':'m', 'time':'s'}) == 27.777755555573332 ,'speed_converter_1 perfectly working!!'

def test_speed_converter_2():
    speed_converter(args = (100,), kwargs = {'dist':'ft', 'time':'s'}) == 91.1388159778361 ,'speed_converter_1 perfectly working!!'

def test_speed_converter_3():
    speed_converter(args = (100,), kwargs = {'dist':'ft', 'time':'s'}) == 91.1388159778361 ,'speed_converter_1 perfectly working!!'

