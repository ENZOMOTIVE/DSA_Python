
my_list = [1,2,4,0,3]


## Shifting problem 
def Selection_Sort(the_list):
  n = len(the_list)
  for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
      if the_list[j] < the_list[min_index]:
        min_index = j
    min_value = the_list.pop(min_index)
    the_list.insert(i, min_value)
  return the_list
  
## Improved Selection Sort with Swaping technique
def Swap_Selection_Sort(the_list):

  n = len(the_list)
  for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
      if the_list[j] < the_list[min_index]:
        the_list[i], the_list[min_index] = the_list[min_index], the_list[i] 
    return the_list


print("This is the normal algo:")
print(Selection_Sort(my_list))


print("This is the improved Algo:")
print(Swap_Selection_Sort(my_list))