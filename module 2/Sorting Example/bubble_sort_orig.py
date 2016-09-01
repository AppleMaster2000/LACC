#!/usr/bin/env python

from graphics import *
import re
import math
import random


def main():
    global sv
    sv = sortVisualizer()
    N = 60
    numbers = list(range(0, N+1))
    
    # randomly shuffle the numbers
    random.shuffle(numbers)
    sv.updateData(numbers)
    numbers = mySort(numbers)   

    # pause until clicked
    sv.win.getMouse()
    
        
def mySort(numbers):
    bubbleSort (numbers)
    sv.updateData(numbers)
    
    sv.win.getMouse()
    
    return numbers



def bubbleSort(List):

#write your code here
#update the graphics every now and then by calling sv.updateData(List)    
    return List

        
if __name__ == "__main__":
	import sys
	import re
	from graphics import *
	from tools import *
main()
    
