#-*- coding:utf-8 -*-

N, M = map(int,raw_input().split())
for i in xrange(1,N,2): 
    print ('.|.'*i).center(N*3,'-')
print 'WELCOME'.center(N*3,'-')
for i in xrange(N-2,-1,-2): 
    print ('.|.'*i).center(N*3,'-')
