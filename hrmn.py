h1,m1=map(int,input().split(' '))
h2,m2=map(int,input().split(' '))
l1=(h1*60)+m1
l2= (h2*60)+m2
tmin=abs(l1-l2)
m = tmin%60
hrs = (tmin - m)/60
print(int(hrs),int(m))
