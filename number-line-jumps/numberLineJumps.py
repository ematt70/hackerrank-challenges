import math
import os
import random
import re
import sys


x1 = 5
x2 = 0
v1 = 1
v2 = 3
same = ""

if x1 > x2 and v1 > v2:
    same = "NO"
elif v2 < v1 and (x2 - x1) % (v2 - v1) == 0:
    same = "YES"
else:
    same = "NO"



print(same)

        
    
    



