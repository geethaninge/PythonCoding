def list_of_prime_numbers_btw_range():
  print("enter a range number for prime no generation:")
  first = int (input("enter First No:"))
  last = int(input("enter last No:"))
  listNum = [x for x in range(first,last+1)]
  print(listNum)
  #prime_num=[]
  base_prime =[2,3,5,7]
  for num in range(first,last+1):
    for initPrime in base_prime:
      if num % initPrime == 0 :
        listNum.remove(num)  
        break
  print("prime numbers between {} to {} is:{} ".format(first,last, listNum))


def listOfPrime_no_2_n():
  last = int(input("enter last No:"))
  list1 = [x for x in range(3,last+1)]
  prime_num =[]
  prime_num.append(2)
  for i in list1[::2]:
    is_prime = True
    for num in prime_num:
      if i%num == 0 :
        is_prime = False
         
    if(is_prime):
      prime_num.append(i)
  print("prime numbers between 2 to {} is:{} ".format(last,prime_num))     
     
#list_of_prime_numbers_btw_range()   
listOfPrime_no_2_n()                  