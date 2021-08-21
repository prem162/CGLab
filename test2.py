import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt
import random
import math
from dual import *
def delet(p):
    p.pop()


def maxim(p):
    print(max(p))

def getArrays():
    return [1,2],[3,4]

n=int(input())
print(n,n*math.log2(n))
