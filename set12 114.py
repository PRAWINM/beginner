N,k=map(int,input().split(" "))
A=list(map(int,input().split(" ")))[:N]
L=[]
for i in A: 
  if(i%2!=0):
    L.append(i)
print(L[k-1])
