N,k=map(int,input().split(" "))
n=[]
for i in range(0,N):
  b=int(input())
  n.append(b)
c=sorted(n)
print(c[k-1])
