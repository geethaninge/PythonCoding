def reverseSortingList():
  print("enter the list items")
  list_item = [int(x) for x in input().split()]
  list_item.sort(reverse=True)
  print("Reversed list items are{}".format(list_item))
        
        
reverseSortingList()              