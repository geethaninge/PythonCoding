def stringRepeatedWords():
  print("enter string:")  
  #list1 = [x for x in input().split()] # for string of words
  list1 = [x for x in input()] # string of letters
  dict1 ={k:list1.count(k) for k in set(list1)}
  dict2 ={}
  dict2.update(dict1)
  for key in dict1:
    value = dict1.get(key)
    if value >1 :
      dict2.pop(key)
  print("String after removing repeated words:")
  print(" ".join(list(dict2)))


stringRepeatedWords()    