# >>> string = "abracadabra"
# >>> print string[5]
# a
# >>> string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   TypeError: 'str' object does not support item assignment
# 
# 
# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
# 
# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new




