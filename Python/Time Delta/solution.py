#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):

    date_format = "%a %d %b %Y %X %z"
    date_obj1 = datetime.strptime(t1, date_format)
    date_obj2 = datetime.strptime(t2, date_format)
    return str(abs(int((date_obj2.timestamp()-date_obj1.timestamp()))))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
