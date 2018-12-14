import textwrap 

def merge_the_tools(string, k):
    # your code goes here
    string_groups = textwrap.wrap(string,k)
    
    for index,item in enumerate(string_groups):
        print item[:index] + item[(index+1):]
    
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)

