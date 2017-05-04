

def allComprehension():
  import sys
  sys.stdout = open("file1.txt", "w+")
  list1 = [x for x in range(1,10)]
  print(list1)
  set1 = {x for x in range(1,5)}
  print(set1)
  dict1 ={ n:n*2 for n in range(5)}
  print(dict1)
  list2 =['ab','cd','ef','gh']
  dict2 = dict(zip(list1,list2))
  print(dict2)
  my_list = ['hello', 'hi', 'hello', 'today', 'morning', 'again', 'hello']
  my_dict = {k:my_list.count(k) for k in my_list}
  print(my_dict)
  
  #with open("file1.txt", "w+") as myFile:
    
  
allComprehension()  
  