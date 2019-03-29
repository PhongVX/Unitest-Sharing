import time
from my_util import utf8_encoding_function
from nonexistent_variable import PI
import nonexistent_library

def sum(num1, num2):
    return num1 + num2


def mul(num1, num2):
    return num1 * num2


def perimeter_of_rectangle(a, b):
    sum_a_b = sum(a, b)
    return sum_a_b * 2


def area_rectangle(a, b):
    return a * b


def area_circle(r):
    return PI * r**2


def max_func(a, b, c, d):
   max=a
   if b>max :
       max=b
   if c>max :
       max=c
   if d>max:
       max=d
   return max

def min_func(a,b,c,d):
   min=a
   if b<min:
       min=b
   if c<min :
       min=c
   if d<min:
       min=d
   return min


def medium(a,b,c,d):
   max=max_func(a,b,c,d)
   min=min_func(a,b,c,d)
   result = list()
   if (max!=a)and(min!=a):
       result.append(a)
   if (max!=b)and(min!=b):
       result.append(b)
   if (max!=c)and(min!=c):
       result.append(c)
   if (max!=d)and(min!=d):
       result.append(d)
   return result


def function_return_multiple_value(num1, num2):
    s = num1 + num2
    m = num1 * num2
    return s, m


def encode_utf8_and_to_lower_string(my_string):
    encode_string = utf8_encoding_function(my_string)
    return '_{}_'.format(encode_string.lower())






