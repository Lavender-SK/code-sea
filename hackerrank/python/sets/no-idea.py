# -*- coding: utf-8 -*-
"""
create time : 2017-08-08 21:15:46
author : sk


"""

n, m = raw_input().split()

array = map(int, raw_input().split())
set_A = set(map(int, raw_input().split()))
set_B = set(map(int, raw_input().split()))

def fun(x):
    if x in set_A:
        return 1
    elif x in set_B:
        return -1
    return 0

print sum(map(fun, array))




