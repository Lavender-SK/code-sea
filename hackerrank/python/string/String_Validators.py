"""
    url: https://www.hackerrank.com/challenges/string-validators?h_r=next-challenge&h_v=zen

    Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

    str.isalnum()
    This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

    str.isalpha()
    This method checks if all the characters of a string are alphabetical (a-z and A-Z).

    str.isdigit()
    This method checks if all the characters of a string are digits (0-9).

    str.islower()
    This method checks if all the characters of a string are lowercase characters (a-z).

    str.isupper()
    This method checks if all the characters of a string are uppercase characters (A-Z).
"""

import re

def pattern_result(string, pattern):
    r = re.findall(pattern,string)
    #print r
    return 'True' if len(r) > 0 else 'False'

if __name__ == '__main__':
    s = raw_input()
    
    # In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
    print pattern_result(s, r'[a-zA-Z0-9]')

    # In the second line, print True if S has any alphabetical characters. Otherwise, print False.
    print pattern_result(s,r'[a-zA-Z]')

    # In the third line, print True if S has any digits. Otherwise, print False. 
    print pattern_result(s,r'[0-9]')
    
    # In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
    print pattern_result(s,r'[a-z]')

    # In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
    print pattern_result(s,r'[A-Z]')
