N,k=map(int,input().split(" "))
n=[]
for i in range(0,N):
  n.append(int(input()))
L=[]
for i in n: 
  if(i%2!=0):
    L.append(i)
print(L[k-1])
