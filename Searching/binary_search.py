
sorted_array = [1,3,6,7,8,9]

search_the_number = 1

def Binary_Search(arr, value):
  
  left = 0
  right = len(arr) - 1
  

  
    
  while left <= right:      
    middle_element = (left + right) // 2
    
    if arr[middle_element] == value:
      print("the number is found", value , "at position" , middle_element)
      return
    
    elif arr[middle_element] < value:
      left = middle_element + 1
      
    else:
      right = middle_element - 1
    
  print("not found")


Binary_Search(sorted_array,search_the_number)
    