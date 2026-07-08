
my_list = [1,2,4,0,3]


def Insertion_Sort(the_list):
  
  n = len(the_list)
  
  
  for i in range(1,n):
  # The element we are inserting
    key = the_list[i]
  # index used to move left
    j = i - 1
  
    while j >= 0 and the_list[j] > key:
      the_list[j+1] = the_list[j]
      j -= 1
    
    the_list[j+1] = key
  
    return the_list
  
  
print(Insertion_Sort(my_list))