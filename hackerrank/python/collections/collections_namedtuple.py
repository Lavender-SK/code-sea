# -*- coding: utf-8 -*-
"""
create time : 2018-09-25 18:27:10
author : sk

code ref:
    https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

Problem:
    collections.namedtuple()
    Basically, namedtuples are easy to create, lightweight object types. 
    They turn tuples into convenient containers for simple tasks. 
    With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Example:
    Code 01:
        >>> from collections import namedtuple
        >>> Point = namedtuple('Point','x,y')
        >>> pt1 = Point(1,2)
        >>> pt2 = Point(3,4)
        >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
        >>> print dot_product
        11
    Code 02:
        >>> from collections import namedtuple
        >>> Car = namedtuple('Car','Price Mileage Colour Class')
        >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
        >>> print xyz
        Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
        >>> print xyz.Class
        Y


Task:
    Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
    Your task is to help Dr. Wesley calculate the average marks of the students.

    average = (sum of all marks) / (total students)

Sample Input:
    TESTCASE 01:
        5
        ID         MARKS      NAME       CLASS     
        1          97         Raymond    7         
        2          50         Steven     4         
        3          91         Adrian     9         
        4          72         Stewart    5         
        5          80         Peter      6   
    TESTCASE 02:
        5
        MARKS      CLASS      NAME       ID        
        92         2          Calum      1         
        82         5          Scott      2         
        94         2          Jason      3         
        55         8          Glenn      4         
        82         2          Fergus     5

Sample Output:
    TESTCASE 01:
        78.00
    TESTCASE 02:
        81.00
"""

stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)

