def largestNumber():
  '''
    Approach # 1 using list 
  '''  
  print("enter three numbers:") 
  list1 = [int(x)for x in input().split()]
  list1.sort(reverse=True)   
  print("the largest number in given numbers is: {}".format(list1[0]))
  
  '''
    Approach # 2 using 3 variables
  ''' 
  num1 = input("enter first number:")
  num2 = input("enter second number:")
  num3 = input("enter third number:")
  large =num1
  if num2>num1 and num2 >num3 :
    large =num2
  elif num3>num1 and num3>num2 :
    large =num3      
  else:
    large =num1
  print("the largest number is :{}".format(large))    
     
largestNumber()  