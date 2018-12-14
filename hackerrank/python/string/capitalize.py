#-*-coding:utf-8-*-

import string as st

def capitalize(string):
    str_list = string.split(' ')
    str_list = map(lambda s : st.capwords(s),str_list)
    return reduce(lambda s1,s2:s1+' '+s2, str_list)

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
