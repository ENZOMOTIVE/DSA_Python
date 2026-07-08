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
    
    
  def pop(self):
  
    if self.size==0:
      print("Nothing to pop, stack is empty")
    popped_value = self.head
    self.head = self.head.next
    self.size -=1
    return popped_value.value
    
  def peek(self):
    print(self.head.value)
    
    
  def isEmpty(self):
    #if self.size == 0
    ## This returns a T or F
    return self.size == 0
    
  def Stacksize(self):  
    return self.size
    
  def print_Stack(self):
  	## Top of the stack
    current_node = self.head
    
    while current_node:
      print(current_node.value, end="->")
      current_node=current_node.next
    print("None")
    
   
   
    
obj = Stack()
 
obj.push(4)
obj.push(5)
obj.push(6)
obj.push(8)
obj.push(9)


obj.peek()
print(obj.pop())
obj.print_Stack()
    
      