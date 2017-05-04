'''
Created on Apr 15, 2017

@author: Geetha
'''

class Stack(object):
  '''
    Stack operation using list 
  '''
  def __init__(self):
    self.items = []
        
  def is_empty(self): 
    return self.items == []

  def push(self,item):  
      self.items.append(item)  #self.items.insert(0,item)
      print("items in stack {}".format(self.items))
      
  def pop(self):
    self.items.pop() # self.items.pop(0)
    print("items in stack {}".format(self.items))
    
  def peek(self): 
     print("the last item of stack")  
     return self.items[len(self.items)-1]
    
  def size(self):
    print("Size of stack")    
    return len(self.items)


s=Stack()
print(s.is_empty())
s.push(4)
s.push(6)
s.push('hi')
s.push('dog')
print(s.peek())
s.pop()
print(s.peek())
print(s.size())
