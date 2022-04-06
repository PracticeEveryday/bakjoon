import sys
import time
N = sys.stdin.readline()

start = time.time() 

numbers = []

numbers = list(map(int, sys.stdin.readline().split()))

# print(numbers)

check_N = int(sys.stdin.readline())

check_list = list(map(int, sys.stdin.readline().split()))

# print(check_list)

for i in check_list :
  if i in numbers :
    print(1)
  else :
    print(0)

end = time.time() 
print(f"{end - start:.5f} sec")

# 이분 탐색으로 다시 풀기