b=int(input())
a=list(map(int,input().split(' ')))[:b]
a.sort()
print("Largest element is:",a[b-1])
