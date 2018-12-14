# -*- coding: utf-8 -*-
"""
create time : 2017-08-06 09:40:08
author : sk


"""

#%%============================================================================
# 1. py-introduction-to-sets
#==============================================================================

from __future__ import division

def average(array):
    # your code goes here
    distinct_array = set(array)
    return round(sum(distinct_array) / len(distinct_array), 3)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result

