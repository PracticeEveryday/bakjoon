# 10951번

while True:
    try:
        A, B= map(int,input().split())
        print(A+B)
    except:
        break
  
# 1152 키 최대값 찾기

word = input().lower()
word_list = list(word)
word_dict = {}
for i in word_list:
  if i not in word_dict :
    word_dict[i] = 1
  else : 
    word_dict[i] += 1

max_word_dict = [k for k, v in word_dict.items() if max(word_dict.values()) == v]
if len(max_word_dict) > 1 :
  print("?")
else :
  print(str(max_word_dict[0]).upper())

lst = list(input().split())
print(len(lst))

# 2908 삼항 연산자 [::-1]

case1, case2 = input().split()

case1 = list(case1)[::-1]
case2 = list(case2)[::-1]

print(''.join(case1)) if int("".join(case1)) > int("".join(case2)) else print(''.join(case2))