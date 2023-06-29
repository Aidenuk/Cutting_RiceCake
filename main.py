
# Approach this question by using parametric search algorithm.
# It is efficient to use it as it reduces time complex O(n) to O(logN)


n = 4 # number of ricecakes
m = 6 # requested numbers from customers.

array = list(map(int,input().split()))

start = 0
end = max(array)

res = 0

while start <=end:
  mid = (start + end) //2
  total = 0
  for x in array:
    if x > mid:
      # sum all the remain parts 
      total += x-mid 
  if total < m:
    # search only the left side 
    end = mid -1 
  else:
    # search the right side
    # record cutter length
    res = mid 
    start = mid+1
print(res)
      
