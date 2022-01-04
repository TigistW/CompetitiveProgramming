#https://www.hackerrank.com/challenges/countingsort1/problem
import math
import os
import random
import re
import sys
def countingSort(arr):
    counter=[0]*(max(arr)+1)
    for i in range(len(arr)):
        counter[arr[i]]=counter[arr[i]]+1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = [0]*(max(arr)+1)
    result = countingSort(arr)
    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
