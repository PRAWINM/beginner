num=int(input("Enter the number:"))
if(num==2):
  print("it is prime")
elif num>2:
  for i in range(2,num):
    if(num%i)==0:
      print("it is not a prime")
      break
    else:
      print("it is prime")
      break
else:
  print("it is prime")
