n=int(input())
l=list(map(int,input().split(' ')))[:n]
for s in l:
    print(s,l.index(s))
