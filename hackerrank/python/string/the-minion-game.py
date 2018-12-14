#-*- coding: utf-8 -*-

def sub_string_count(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string))) 

# Terminated due to timeout
# def minion_game(string):
#     str_vowel='AEIOU'
#     ready_list = []
#     Stuart_score = 0
#     Kevin_score = 0
# 
#     for i in range(len(string)):
#         if string[i] in str_vowel:
#             for j in range(i+1,len(string)+1):
#                 if string[i:j] not in ready_list:
#                     ready_list.append(string[i:j])
#                     Kevin_score += sub_string_count(string,string[i:j])
#         else:
#             for j in range(i+1,len(string)+1):
#                 if string[i:j] not in ready_list:
#                     ready_list.append(string[i:j])
#                     Stuart_score += sub_string_count(string,string[i:j])  
#     if Stuart_score > Kevin_score:
#         print 'Stuart', Stuart_score
#     elif Stuart_score < Kevin_score:
#         print 'Kevin', Kevin_score
#     else:
#         print 'Draw'

def minion_game(string):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)
    
    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
