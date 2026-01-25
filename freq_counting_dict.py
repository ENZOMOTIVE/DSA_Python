my_array = [5,2,3,8,8,1]

freq = {}

test = {}
test1 = {}
test[5] = 1
print(test)
for x in my_array:
  freq[x] = freq.get(x,0) + 1
  
for x in my_array:
  if x in test1:
    test1[x] += 1
  else:
    test1[x] = 1
  
print(freq)
print(test1)
  