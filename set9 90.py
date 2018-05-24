N=list(input())
a=[]
for i in N:
    if(i.isdigit()):
      a.append(i)
print("".join(str(N) for N in a))
