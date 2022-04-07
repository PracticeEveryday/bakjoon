import sys

N = int(sys.stdin.readline())
numbers_list = []

for i in range(N):
  number = int(sys.stdin.readline())
  numbers_list.append(number)

numbers_list.sort()

for i in numbers_list:
  print(i)