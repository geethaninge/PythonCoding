def factorial():
  num = int(input("enter number  : "))
  if num==1 or num==0 :
    print("Factorial of {} is {}".format(num,num))
  else:
    for i in range(2,num):
      num = num*i
    print("Factorial of given number is {}".format(num)) 
    
factorial()       