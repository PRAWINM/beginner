N,K=map(int,input().split(" "))
L=list(map(int,input().split(" ")))[:N]
a=[]
for K in L:
  a.append(K)
print(a.count(K))
