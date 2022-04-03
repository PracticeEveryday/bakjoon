# num = int(input())

# for i in range(1, 10):
#   print(f'{num} * {i} = {num*i}')

# case = int(input())

# for i in range(case) :
#   a, b = map(int, input().split())
#   print(a+b)

# num = int(input())
# add = 0

# for i in range(num + 1):
#   add += i

# print(add)

# import sys  # sys모듈 읽어들이기

# num = int(sys.stdin.readline())

# for i in range(num):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# num = int(input())

# for i in range(1, num+1):
#   print(i)

# num = int(input())

# for i in range(num) :
#   print(num-i)

# case = int(input())

# for i in range(case):
#   a, b = map(int, input().split())
#   print(f'Case #{i+1}: {a+b}')

# case = int(input())

# for i in range(case):
#   a, b = map(int, input().split())
#   print(f'Case #{i+1}: {a} + {b} = {a+b}')

# num = int(input())

# for i in range(1, num+1):
#   print('*'*i)

# num = int(input())

# for i in range(1, num + 1):
#   print((' ' * (num - i))+("*"*i))

# N, X = map(int, input().split())

# arr = list(map(int, input().split()))
# result = []

# for i in range(N):
#   if arr[i] < X :
#     result.append(arr[i])
# print(*result)

# while True : 
#   a, b = map(int, input().split())

#   if a == 0 and b == 0 :
#     break

#   print(a + b)


# while True:
#     try:
#         A, B= map(int,input().split())
#         print(A+B)
#     except:
#         break
  
num = input()

cnt = 1

if int(num) < 10 :
  num = "0" + num

num_list = list(map(int, list(num)))

def add_list(num_list) :
  result = num_list[0] + num_list[1]
  if result >= 10:
    result -= 10
    return str(num_list[1]) + str(result)
  else : 
    return str(num_list[1]) + str(result)

while True :
  num2 = num
  result = add_list(num_list)
  if num2 == result :
    break
  else :
    cnt += 1
    num_list = list(map(int, list(result)))

print(cnt)






