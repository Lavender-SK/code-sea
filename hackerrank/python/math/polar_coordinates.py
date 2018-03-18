# -*- coding: utf-8 -*-
"""
create time : 2018-01-23 21:57:18
author : sk


"""

import re
from cmath import *

if __name__ == "__main__":
    re, im = map(float, re.findall('[+-]?\d+\.?\d*', input().strip()))
    print(abs(complex(1.0, 2.0)))
    print(phase(complex(1.0, 2.0)))

