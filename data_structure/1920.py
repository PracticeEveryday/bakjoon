# import sys
# import time
# N = sys.stdin.readline()

# start = time.time() 

# numbers = []

# numbers = list(map(int, sys.stdin.readline().split()))

# # print(numbers)

# check_N = int(sys.stdin.readline())

# check_list = list(map(int, sys.stdin.readline().split()))

# # print(check_list)

# for i in check_list :
#   if i in numbers :
#     print(1)
#   else :
#     print(0)

# end = time.time() 
# print(f"{end - start:.5f} sec")

# 이분 탐색으로 다시 풀기

import sys
import time

N = sys.stdin.readline()

start = time.time()
number = sorted(map(int, sys.stdin.readline().split()))

check_N = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

def binary_search(i , number, start, end):
  if start > end :
    return 0
  
  m = (start + end) // 2
  if i == number[m]:
    return 1
  elif i < number[m]:
    return binary_search(i, number, start, m-1)
  else :
    return binary_search(i, number, m+1, end)

for i in check_list:
  start = 0
  end = len(number)-1
  print(binary_search(i, number, start, end))


end = time.time() 
print(f"{end - start:.5f} sec")