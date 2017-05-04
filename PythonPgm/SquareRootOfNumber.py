'''
The square root of n is n^1/2 which is n**0.5
'''
def squareRoot():
  num = int(input("enter a number:"))
  if num <0 :
    print("enter positive number")
  else:
    squareroot =num**0.5;
    print("The square root of {} is{}".format(num,squareroot))
    
squareRoot()      