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

A, B ,V = map(int, input().split())

can_oneday = A - B

if (V-A) % can_oneday == 0:
  duration = int((V-A) / can_oneday)
else :
  duration = int((V-A) / can_oneday +1)
print(duration + 1)


# A, B, V = map(int, input().split())
 
# high = V - A
# if high % (A-B) == 0:
#     first = int(high/(A-B))
# else:
#     first = int(high/(A-B) + 1)
# print(first + 1)