def Bubble_Sort(the_list):
  
  n = len(the_list)
  for i in range(n-1):
    Swap = False
    
    for j in range(n-1 - i):
      if the_list[j+1] < the_list[j]:
    # Swapped
        the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
        Swap = True
    if Swap == False:
      break
  return the_list
    

def Selection_Sort(the_list):
  n = len(the_list)
  for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
      if the_list[j] < the_list[min_index]:
        min_index = j
        
    the_list[i], the_list[min_index] = the_list[min_index], the_list[i]
  return the_list
  
  
def Insertion_Sort(the_list):
  n = len(the_list)
  
  for i in range(1,n):
    insert_index = i
    current_value = the_list[i]
    for j in range( i-1, -1 , -1):
      if the_list[j] > current_value:
        the_list[j+1] = the_list[j]
        insert_index = j
      else:
        break
        
    the_list[insert_index] = current_value
    
    return the_list
    
    
  
input_list = [1,4,2,6,3]
 
print(Bubble_Sort(input_list))
print(Selection_Sort(input_list))
print(Insertion_Sort(input_list))