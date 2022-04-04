# num = int(input())

# lst = list(map(int, input().split()))

# print(min(lst), max(lst))

# case = 9
# max_index = 0
# max_number = 0
# lst=[]
# for i in range(case) :
#   lst.append(int(input()))

# max_number = max(lst)
# max_index = lst.index(max_number)
# print(max_number)
# print(max_index + 1)

# a = int(input())
# b = int(input())
# c = int(input())

# number_dict = {}
# mul = a * b * c

# for i in list(str(mul)):
#   if i not in number_dict :
#     number_dict[i] = 1
#   else : 
#     number_dict[i] += 1


# for i in range(0, 10) :
#   i = str(i)
#   if i in number_dict :
#     print(number_dict[i])
#   else : 
#     print(0)

# case = 10

# unoverlap = []

# for i in range(10):
#   num = int(input())
#   remainder = num % 42  
#   if remainder not in unoverlap :
#     unoverlap.append(remainder)
#   else :
#     pass

# print(len(unoverlap))

# case = int(input())
# score_lst = list(map(int, input().split()))

# new_lst = []

# max_score = max(score_lst)


# for i in range(case):
#   new_lst.append(round(score_lst[i]/max_score * 100, 2))

# sum_data = sum(new_lst)
# print(f'{sum_data/len(new_lst)}')

# case_num = int(input())
# sum_O = 0
# for i in range(case_num):
#   sum_O = 0
#   case = input()
#   case_list = case.split('X')

#   for j in range(len(case_list)):
#     for z in range(1, len(case_list[j])+1):
#       sum_O += z
#   print(sum_O)

case = int(input())

for i in range(case):
  case_list = list(map(int, input().split()))
  case_personnel = case_list.pop(0)
  persons = []
  case_average = sum(case_list) / case_personnel


  for j in range(case_personnel):
    if case_list[j] > case_average :
      persons.append(case_list[j])
  
  #print(str(round(len(persons)/case_personnel * 100, 3))+"%")
  print('{:.3f}%'.format(len(persons)/case_personnel * 100))
