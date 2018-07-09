b=int(input())
a=list(map(int,input().split(' ')))[:b]
a.sort()
print(a[0])
