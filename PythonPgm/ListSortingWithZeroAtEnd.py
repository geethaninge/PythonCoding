def listSortWithZeroAtEnd():
  print("enter element to list:")
  list1 = [int(x) for x in input().split()]
  list2=[]
  count=0
  '''  list3=[]
  for i in range(len(list1)):
    if list1[i] == 0:
      list2.append(list1[i])
    else:
      list3.append(list1[i]) 
  print("list2 : {} and list 3 : {}".format(list2,list3))
  list3.sort()  
  list3.extend(list2)
  print(list3) 
  ''' 
  for num in list1:
    if num == 0:
      count+=1
    else:
      list2.append(num)
  list2.sort()
  for i in range(count):
    list2.append(0)
  print(list2)         
    
 
  
listSortWithZeroAtEnd()