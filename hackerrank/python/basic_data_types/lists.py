# -*- coding: utf-8 -*-

if __name__ == "__main__":
    List = []
    N = int(raw_input())

    for i in range(N):
        op = raw_input().strip().split()
        if op[0] == 'insert':
            List.insert(int(op[1]), int(op[2]))
        elif op[0] == 'print':
            print List
        elif op[0] == 'remove':
            List.remove(int(op[1]))
        elif op[0] == 'append':
            List.append(int(op[1]))
        elif op[0] == 'sort':
            List.sort()
        elif op[0] == 'pop':
            List.pop()
        elif op[0] == 'reverse':
            List.reverse()

