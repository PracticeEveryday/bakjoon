'''
num = int(input())
count = 0
while num != 1:
  if num % 3 != 0 and num % 2 == 0 :
    num = num - 1
    count += 1
    print('1 :',num, count)
  elif num % 3 == 0:
    num = num // 3
    count += 1
    print('2 :',num, count)
  elif num % 2 ==0 :
    num = num // 2
    count += 1
    print('3 :',num, count)
    
print(count)
시간 초과.
동적 계획법 이용해야함
동적 계획법?
-> 이미 진행된 연산이 반복되는 결점을 보완하기 위해 고안됨.
여러 개의 소문제로 분할하여 각 소문제의 해결안을 바탕으로 주어진 문제를 해결,! 이 때 각 소문제는 다시 여러개의 소문제로 분할 가능하다.

1. 처음 진행되는 연산은 기록
2. 이미 진행됬던 연산이라면 다시 연산이라면 기록되어 있는 값을 호출
3. 시간 & 자원절약 가능
'''

num = int(input())
dp = [0 for i in range(num+1)]
print(dp)

for i in range(2, num+1):
  dp[i] = dp[i-1] + 1

  if i%2 == 0 and dp[i] > dp[i//2] +1 :
    dp[i] = dp[i//2] + 1

  if i%3 == 0 and dp[i]> dp[i//3] +1 :
    dp[i] = dp[i//3] +1

print(dp)
print(dp[num])