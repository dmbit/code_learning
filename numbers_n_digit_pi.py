# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:49:44 2018

@author: daiman
"""
# mega projects
# numbers
# first one : Find PI to the Nth Digit 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.
from decimal import *
import math
def factorial(n):
    "return fatorial of n using recursion"
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        
def get_k_number_of_pi(k):    
    "use chudnovsky algorithm"
    getcontext().prec=k # 设置精度（有效数字位数）
    temp_sum=0
    for i in range(k+1):
        up=factorial(6*i)*(13591409 + 545140134*i)
        down=factorial(3*i)*(factorial(i)**3)*((-640320)**(3*i))
        temp_sum+=up/down
    c=Decimal(426880 * math.sqrt(10005))
    return c/Decimal(temp_sum)
def shell():
    while True:
        k=input("please enter the number of pi digits you want to calcaulate or enter q to quit:")
        if k=="q":
            break
        else:
            print(get_k_number_of_pi(int(k)))
    print("that is the end.")
if __name__=="__main__":
    shell()       