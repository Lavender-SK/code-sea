# -*- coding: utf-8 -*-

#%%============================================================================
#
#==============================================================================

dict_info = {}

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    dict_info[name] = score    

second_min_value = sorted(set(dict_info.values()))[1]

result = sorted([key for key, value in dict_info.items() if value == second_min_value])

for i in result:
    print i








