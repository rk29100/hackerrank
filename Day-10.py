#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    result = 0
    high = 0

    while n > 0:


        if n % 2 == 1:
            result += 1
            if result > high:
                high = result

        else:
            result = 0

        n=n//2 

    print(high)
