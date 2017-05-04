def serachWordInString():
    '''
      Approach #1 using Strings 
    '''
    """string=input("enter string :").split()
    searchTerm =input("enter search term:")
    for word in string[::]:
        if word== searchTerm :
          print("the search term :{} is found at position:{}".format(searchTerm,string.index(word)))
          break
        else:
          print("the search term: {} is not found in String:{}".format(searchTerm,string))"""
          
    '''
      Approach #2 using List 
    '''  
    print("enter String")                
    list1 = [x for x in input().split()]  
    term = input("enter search term:")
    if list1.index(term) :
        print("search term is found at index :{}".format(list1.index(term)))
    else:
        print("search term is not found in string")    
        
    
    
    
       
serachWordInString()            