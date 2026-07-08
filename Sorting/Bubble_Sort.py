
my_list = [1,2,3,4,5]

def bubble_sort(the_list):
  
  n = len(the_list)
  temp = 0
  
  for i in range(n-1):
    swapped = False
    for j in range(n-1-i):
      if the_list[j] > the_list[j+1]:
        temp = the_list[j] 
        the_list[j] = the_list[j+1]
        the_list[j+1] = temp
        swapped = True
        
        # or
        # the_list[j] , the_list[j+1] = the_list[j+1], the_list[j]
    swapped = True
    
    if swapped is False:
      break
        
  return the_list
  

  
  
print(bubble_sort(my_list))
  