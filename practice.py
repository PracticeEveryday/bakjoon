# a = int(input())
# b = int(input())

# print(a + b)

# N = int(input())

# number_list = list(map(int, input().split()))

# decimal = []

# for i in number_list:
#   remain = []
#   for j in range(1, i+1):
#     remain.append(i%j)
#   if len([i for i in remain if i == 0]) == 2:
#     decimal.append(i)

# print(len(decimal))

# A, B ,V = map(int, input().split())

# can_oneday = A - B

# if (V-A) % can_oneday == 0:
#   duration = int((V-A) / can_oneday)
# else :
#   duration = int((V-A) / can_oneday +1)
# print(duration + 1)

# weight = int(input())

# count = 0

# while weight >= 0:

#   if weight % 5 == 0:
#     count += weight // 5
#     weight = 0
#  
#   weight -= 3
#   count += 1
# if(weight != 0) :
#   print(-1)
# else : 
#   print(count)

# N = int(input())
# for i in range(N):
#   room = []
#   length, width, number = map(int, input().split())
#   for j in range(1, width+1) :
#     for k in range(1, length+1) :
#       room.append(str(k) + str(j).zfill(2))
#   print(room[number-1])

# score = []
# for i in range(5):
#   score.append(int(input()))

# for i in range(len(score)) :
#   if score[i] < 40 :
#     score[i] = 40
    
# print(sum(score)//5)

# x, y, w, h = map(int, input().split())

# print(min(x, y, w-x, h-y))

# case = int(input())


# for i in range(case) :
#   height = int(input())
#   people = int(input())
#   zfloor = [x for x in range(1, people+1)]
#   upfloor = []
#   #print(zfloor)
#   for i in range(height):
#     for j in range(1, people):
#       zfloor[j] += zfloor[j-1]
#   #print(zfloor)
#   print(zfloor[-1])

# A = list(map(int, input().split()))

# B = min(A)
# C = max(A)

# A.pop(A.index(B))
# A.pop(A.index(C))

# print(*A)

# N = int(input())

# for i in range(N) :
#   print("*"*(N-i))


''''
  a**2 + b**2 = c**2
'''

while True:
  A, B, C = map(int, input().split())
  arr = [A, B, C]
  if A == 0 and B == 0 and C == 0 :
    break
  hypotenuse = max(A, B, C)
  idx = arr.index(hypotenuse)
  arr.pop(idx)
  # print(arr)
  N = arr[0]
  M = arr[1]

  # print(N, M, hypotenuse)

  if hypotenuse ** 2 == N ** 2 + M ** 2:
    print("right")
  else :
    print("wrong")