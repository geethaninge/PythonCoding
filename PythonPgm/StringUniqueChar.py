def stringUniqueChar():
  from collections import OrderedDict  
  str1 = input("enter a string:")
  # without using set
  unique =[]
  for char in str1[::]:
    if char not in unique:
      unique.append(char)
  print(unique)
  print(len(unique))
  """list1 = list(set(str1))
  print(list1)"""
  # with OrderedDict
"""  od = OrderedDict.fromkeys(str1).keys()
  print(list(od))
  print(len(list(od)))
  print("".join(od))"""

      
stringUniqueChar()  