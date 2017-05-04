class DeQueue(object):
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    if self.items == []:
      print("DeQueue is empty!")
      
  def addFront(self,item):
    self.items.append(item)
    print("{} added to the front of dequeue".format(item))  
    print("items in dequeue :{}".format(self.items)) 
    
  def addEnd(self,item):
    self.items.insert(0,item)
    print("{} added to the end of dequeue".format(item))  
    print("items in dequeue :{}".format(self.items))   
            
  def removeFront(self):
    self.items.pop()  
    print("items in dequeue : {}".format(self.items))    
           
  def removeEnd(self):       
    self.items.pop(0)  
    print("items in dequeue : {}".format(self.items))
    
  def size(self):
    print("size of dequeue:{}".format(len(self.items)))
      
d =  DeQueue()
d.isEmpty()
d.addFront(4)
d.addFront(5)
d.addEnd("hi")
d.size()
d.removeEnd() 
d.removeFront()  
                