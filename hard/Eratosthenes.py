
'''
A, B = map(int, input().split())

A_B = list(range(A, B+1))

for i in A_B:
  remain = []
  for j in range(i+1):
    if j != 0:
      remain.append(i % j)
  if remain[0] == 0 and remain[len(remain)-1] == 0 and 0 not in remain[1:len(remain)-1] :
    print(i)
시간 초과

# 에라토스테네스의 채
=> 1 지운다, 2는 소수 2의 배수는 다 지운다. 3은 소수 3의 배수는 다 지운다 ~~
범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
1. 1은 제거 
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다. 
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다. 
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다. 
5. (반복)
-> 제곱근만 약수의 여부를 검증해도 된다!
-> 시간복잡도인 O(N)에서 O(N^(1/2))로 줄게되어 시간이 단축된다.
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
'''

import math

A, B = map(int, input().split())

A_B = list(range(A, B+1))

def sieve_of_Eratosthenes (num):
  if num == 1 :
    return False
  else :
    for i in range(2, math.floor(math.sqrt(num))+1):
      if num % i == 0:
        return False
    return True

for i in A_B:
  if sieve_of_Eratosthenes(i):
    print(i)
  
