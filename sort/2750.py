N = int(input())
numbers_list = []

for i in range(N):
  number = int(input())
  numbers_list.append(number)

numbers_list.sort()

for i in numbers_list:
  print(i)