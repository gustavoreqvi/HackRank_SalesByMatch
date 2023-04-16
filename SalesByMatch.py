#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    lst_set_ar = set(ar)
    if ( n >= 1 and n <= 100):
      len_ar = len(ar)
      if (len_ar >= 0 and len_ar <= n):
        total_counting_pair = 0
        for i in lst_set_ar:
          counting = ar.count(i)
          counting_pair = counting//2
          total_counting_pair = counting_pair + total_counting_pair
        return total_counting_pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
