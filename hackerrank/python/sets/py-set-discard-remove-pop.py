# -*- coding: utf-8 -*-
"""
create time : 2017-08-15 21:14:57
author : sk


"""

n = input()
s = set(map(int, raw_input().split())) 

commands_num = input()

for i in range(commands_num):
    command = raw_input().split()
    if command[0] == 'pop':
        s.pop()
    if command[0] == 'remove':
        s.remove(int(command[1]))
    if command[0] == 'discard':
        s.discard(int(command[1]))
print sum(s)



