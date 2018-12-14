# -*- coding: utf-8 -*-
"""
create time : 2017-08-06 10:28:34
author : sk


"""

#%%============================================================================
# 
#==============================================================================

set_a_N = raw_input()
set_a = set(map(int,raw_input().split()))

set_b_N = raw_input()
set_b = set(map(int,raw_input().split()))

set_result = sorted(set_a.difference(set_b).union(set_b.difference(set_a)))

print '\n'.join(map(str,set_result))



