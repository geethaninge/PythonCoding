def stringUniqueWord():
  """enter String:
  calvin klein design dress calvin klein """   
  from collections import OrderedDict  
  print("enter String:")
  list1 = [x for x in input().split()]
  print(list1)
  print(set(list1))

  od = OrderedDict.fromkeys(list1).keys()
  print(" ".join(od))
  unique =[]
  for word in list1[::]:
    if word not in unique:
      unique.append(word)
  print(unique)

stringUniqueWord()  