M = int(input())
N = int(input())

import math

M_N = list(range(M, N+1))
# print(M_N)
value = []
def Eratosthenes(num) :
  if num == 1 :
    return False
  else :
    for i in range(2, math.floor(math.sqrt(num))+1) :
      if num % i == 0 :
        return False
    return True

for i in M_N :
  if Eratosthenes(i) :
    value.append(i)

if len(value) == 0 :
  print(-1)
else :
  # print(value)
  print(sum(value))
  print(min(value))

