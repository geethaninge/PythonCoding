def fibanocci():
  fib = []
  #fib.insert(0,1)
  #fib.insert(1,1)
  fib.append(1)
  fib.append(1)
  n= int(input("enter max number:"))
  for i in range(1,n-1):
    #fib.insert(i+1,fib[i]+fib[i-1])
    fib.append(fib[i]+fib[i-1])
  print(fib)    
    
fibanocci()    
      