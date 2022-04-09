'''
N = int(input())

value = []

for i in range(N) :
  value.append(int(input()))

value.sort()

for i in value :
  print(i)
메모리 초과
'''

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 모든 입력을 배열에 저장하면 당연히 메모리 초과입니다. 문제의 메모리 제한은 겨우 8MB입니다. 아무리 작은 자료형으로 저장한다고 해도 short형 (2바이트) 천만 개면 약 20MB로 역시 메모리 초과입니다. 입력을 전부 저장하지 않고 푸는 방법을 생각해 보세요. 힌트는 입력되는 정수의 범위에 있습니다.

import sys
N = int(sys.stdin.readline())

value = [0] * 10001
idx = []
# print(len(value), value[293])
result_value = []
for i in range(N):
  number = int(sys.stdin.readline())
  if value[number-1] == 0:
    value[number-1] = 1
  idx.append(number-1)
# print(value)

idx.sort()
# print(value)
# print(idx)

# for i in range(len(value)):
#   if value[i] != 0:
#     for j in range(value[i]):
#       print(i+1)
# print(type(idx[1]))
for i in idx:
  print(value[i] * (i+1))
