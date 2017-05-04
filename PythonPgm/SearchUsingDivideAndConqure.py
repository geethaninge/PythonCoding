'''
Divide and conqre approach has log n time complexity
for binary search string should be in sorted order
'''
def binarySearch(list1,key):
  
  if len(list1)==0 :
    return False    
  mid = (len(list1))//2
  if key == list1[mid] :
    return True
  elif key < list1[mid]:
    return binarySearch(list1[:mid-1],key)
  else:
    return binarySearch(list1[mid+1:],key)  
   
  
list1= [int(x) for x in input("enter elements :").split()]

key =int( input("enter search element :"))
position =binarySearch(list1.sort(),key)
if position :
  print("the search term is found ")
else:
  print("the search term is not found ")  