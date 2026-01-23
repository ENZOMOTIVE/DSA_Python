## Stack Implementation using Linked List

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
    
class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
    
  def push(self, value):
    new_node = Node(value)
       
  	## Link the new node to the previous element
    new_node.next= self.head
    ## Move the head to the new node 
    self.head =new_node
    
      ## Increase the size as the item is added
    self.size += 1
    
  def peek(self):
    print(self.head.value)
    
   
   
    
obj = Stack()
 
obj.push(4)
obj.push(5)
obj.peek()
    
      