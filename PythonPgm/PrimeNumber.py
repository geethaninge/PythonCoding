def primeNumber():
  num = int( input("enter a number: "))
  for i in range(2,num):
    if num%i == 0:
      return False
  return True   


is_prime = primeNumber()
if(is_prime):
  print("the given number is prime number") 
else:
  print("the given number is not a prime number")        