# -*- coding: utf-8 -*-

#### 1. 
# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.wrap(string,8)
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']

# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.fill(string,8)
# This is
# a very
# very
# very
# very
# very
# long
# string.

#### 2. code 

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result 
