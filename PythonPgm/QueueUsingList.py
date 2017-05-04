'''
Created on Apr 15, 2017

@author: Geetha
'''

class Queue(object):
  def __init__(self):
    self.items = []
   
  def isEmpty(self):  
    if self.items == []:
      print("Queue is empty!")

  def enQueue(self,item):
    print("{} inserted to queue".format(item))
    self.items.insert(0,item)  
    print("items in queue : {}".format(self.items))
    
  def deQueue(self):
    self.items.pop()
    print("items in queue : {}".format(self.items))
    
  def size(self):
    print("size of queue:{}".format(len(self.items))) 
    
qe= Queue()
qe.isEmpty()
qe.enQueue("hi")
qe.enQueue(4)
qe.enQueue("dog")
qe.size()
qe.deQueue()
qe.deQueue()

 
    
       
  
    
        