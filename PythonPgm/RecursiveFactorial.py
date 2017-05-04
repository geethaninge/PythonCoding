def recursiveFact(n):
  if n==0 or n==1 :
    return 1
  else:
    return n*recursiveFact(n-1)      
    
fact =recursiveFact(5)
print("factorial of number is {}".format(fact))   