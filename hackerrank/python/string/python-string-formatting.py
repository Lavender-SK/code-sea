#-*-coding:utf-8-*-

# https://docs.python.org/2/library/string.html

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in xrange(1,n+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)




