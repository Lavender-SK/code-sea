# -*- coding: utf-8 -*-
"""
create time : 2018-09-20 22:42:51
author : sk

code ref:
    https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
        
Problem:
    The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want. 

For example:
    from collections import defaultdict
    d = defaultdict(list)
    d['python'].append("awesome")
    d['something-else'].append("not relevant")
    d['python'].append("language")
    for i in d.items():
        print(i)

result:
    ('python', ['awesome', 'language'])
    ('something-else', ['not relevant'])

question:
    in this challenge, you will be given 2 integers, n and m. There are nwords, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.    

"""

from collections import defaultdict
d = defaultdict(list)

result = ''

n,m = map(int, input().split())

for i in range(n):
    d[input()].append(i+1)

for i in range(m):
    s = input()
    if s in d:
        result += " ".join(map(str, d[s])) + "\n"
    else:
        result += "-1" + "\n"

print(result[0:-1])
