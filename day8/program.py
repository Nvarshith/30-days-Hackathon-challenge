import sys
n = int(input())
phonebook={}
for i in range(n):
    contact=input().split(' ')
    phonebook[contact[0]]=contact[1]
lines=sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phonebook:
        print(name + '=' + str( phonebook[name] ))
    else:
        print('Not found')
