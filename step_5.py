# def add(lst):
#   return sum(lst)

# print(add(list(map(int, input().split()))))

# numbers = list(range(1, 10001))
# remove_list = []  
# for num in numbers :
#     for n in str(num):
#         num += int(n)  
#     if num <= 10000:  
#         remove_list.append(num)  

# for remove_num in set(remove_list) : 
#     numbers.remove(remove_num)
    
# for self_num in numbers :  
#     print(self_num)

num = int(input())

count = 0


for i in range(num) :
  if num < 100 :
    count += 1
  else :
    count = 99
    for i in range(100, num+1) :
      strNum = str(i)
      listNum = list(strNum)
      one = int(listNum[0]) - int(listNum[1])
      two = int(listNum[1]) - int(listNum[2])
      if one == two :
        count += 1
print(count)