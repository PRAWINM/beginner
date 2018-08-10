N=int(input())
array=list(map(int,input().split(",")))[:N]
array1=[]
for i in array:
  array1.append(int(i))
count=0
for i in array1:
  for j in array1:
    for k in array1:
      if (i!=j and j!=k and k!=i):
        count+=1
c=(count//6-5)
print(abs(c))
