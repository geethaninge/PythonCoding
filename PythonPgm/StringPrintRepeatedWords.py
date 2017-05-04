def stringRepeatedWords():
  print("enter string:")  
  list1 = [x for x in input().split()]
  dict1 ={k:list1.count(k) for k in set(list1)}
  for key in dict1:
    value = dict1.get(key)
    if value >1 :
      print("Repeated word in string is :{}".format(key))


stringRepeatedWords()    
"""enter string:
calvin klein design dress calvin klein"""