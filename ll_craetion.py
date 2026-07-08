class Node:
  def __init__(self, value): 
    self.value = value
    self.next = None


def build_ll(value):
  head = Node(value[0])
  
  current = head
  
  for i in value[1:]:
    current.next = Node(i)
    current = current.next
  return head


def traverse_ll(head):
  while head:
    print(head.value, "->", end = " ")
    head = head.next
  print("None")
  
  
def find_min_value(head):
  
  min_value = head.value
  
  while head:
    if head.value < min_value:
      min_value = head.value      
    head = head.next
    
  print("The smallest element in the list is", min_value)

def find_max_value(head):
  max_value = head.value
  
  while head:
    if head.value > max_value:
      max_value = head.value      
    head = head.next
    
  print("The largest element in the list is", max_value)
  

    
def delete_node(target, head):
  # Case1: When the head is empty
  if not head:
    return head
  
  #Case 2: head == target
  if head.value == target:
    return head.next
  
  #Case3: when node is at an arbitrary point
  current = head
  
  while current.next:
    if current.next.value == target:
      current.next = current.next.next
      return head
    current = current.next
    
  return head
  
      
  



input_values = [1,2,3,4,45,5,0]


the_head = build_ll(input_values)

the_head = delete_node(5,the_head)

delete_node(the_head,the_head)
traverse_ll(the_head)
find_min_value(the_head)
find_max_value(the_head)
