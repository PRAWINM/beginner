N,k=map(int,input().split(" "))
A=list(map(int,input().split(" ")))[:N]
c=sorted(A)
print(c[k-1])
