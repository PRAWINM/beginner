n=int(input("Enter the size:"))
l=list(map(int,input("Enter the values:").split(' ')))
for s in l:
    print(s,l.index(s))
