## Frequency of each element appearing in the list


my_list = [1,2,2,3,3,4,4,4,5]




def Freq_counter(the_list):
  freq = {}
  
  for i in the_list:
    
    freq[i] = freq.get(i,0) + 1
    
  return freq
  
  
def Number_1Freq(the_list, freq):
  result = []
  for i in the_list:
    if freq[i] == 1:
      result.append(i)
  return result


print(Freq_counter(my_list))

the_freq = Freq_counter(my_list)
print(Number_1Freq(my_list, the_freq))