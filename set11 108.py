N,K=map(int,input().split(" "))
L=list(map(int,input().split(" ")))[:N]
c=sorted(L)
print(c[K-1])
