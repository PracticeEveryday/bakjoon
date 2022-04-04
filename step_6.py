# word = input()
# print(ord(word))

# case = int(input())
# case_str = list(input())

# print(sum(list(map(int, case_str))))

# word_lst = list(input())

# alphabet = list('abcdefghijklmnopqrstuvwxyz')
# alphabet_dict = {}
# result = []
# for i in range(len(alphabet)):
#   alphabet_dict[alphabet[i]] = -1

# for i in range(len(word_lst)):
#   if(alphabet_dict[word_lst[i]] == -1):
#     alphabet_dict[word_lst[i]] = i

# for key in alphabet_dict:
#   result.append(alphabet_dict[key])
# print(*result)

# case = int(input())
# lst = []
# for i in range(case):
#   count, word = input().split()
  
#   for j in range(len(word)) :
#     lst.append(word[j]*int(count))
#   print("".join(lst))
#   lst = []

# word = input().lower()
# word_list = list(word)
# word_dict = {}
# for i in word_list:
#   if i not in word_dict :
#     word_dict[i] = 1
#   else : 
#     word_dict[i] += 1

# max_word_dict = [k for k, v in word_dict.items() if max(word_dict.values()) == v]
# if len(max_word_dict) > 1 :
#   print("?")
# else :
#   print(str(max_word_dict[0]).upper())

# lst = list(input().split())
# print(len(lst))

# case1, case2 = input().split()

# case1 = list(case1)[::-1]
# case2 = list(case2)[::-1]

# print(''.join(case1)) if int("".join(case1)) > int("".join(case2)) else print(''.join(case2))

# word = list(input().upper())

# duration = []

# dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# for i in word:
#   for j in range(len(dial)) :
#     if i in dial[j]:
#       duration.append(j+3)

# print(sum(duration))

# croatia = ['c=', 'c-', 'dz=', 'd-', 'nj', 'lj', 's=', 'z=']

# word = input()
# exist = []

# word2 = word
# for i in croatia:
#   if i in word :
#     exist.append(i)
  
#     if i == 'dz=' :
#       word = word.replace(i, '')
  

# print(exist)
# print(len(word2) - len(''.join(exist)) + len(exist))

# # for i in croatia :
# #   word = word.replace(i, 'i')

# # print(len(word))

case = int(input())
count = case

for i in range(case) :
  word = input()
  for j in range(0, len(word)-1):
    if word[j] == word[j+1]:
      pass
    elif word[j] in word[j+1:]:
      count -= 1
      break

print(count)
