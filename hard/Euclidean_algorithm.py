# 유클리드 호제법

# 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘
# 호제법이란 서로 상대방 수를 나누어 결국 원하는 수를 얻는 알고리즘.
# 두개의 자연수 A, B에 대해서 A를 B로 나눈 나머지를 R이라고 한다(단, A>B) A와 B의 최대 공약수는 B와 R의 최대공약수와 같다.
# 이 성질에 따라 B를 R로 나눈 나머지 R'를 구하고 다시 R을 R'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 A와 B의 최대공약수이다.

# a와 b의 최대 공약수는 (a를 b로 나눈 나머지와) b의 최대공약수와 같다.

a, b = 315, 495
if (b > a) :
  a, b = b, a

while(b != 0):
  a = a % b
  a, b = b, a

print(a)

# a, b의 최대 공약수는 (a - b), b 의 최대공약수와 같다.

a, b = 315, 495

while(a != b) :
  if(a > b) :
    a -= b
  else : 
    b -= a
print(a)

A, B = map(int, input().split())
addAB = A * B
if B > A :
  A, B = B, A

# print(A, B)

while(B != 0) :
  r = A % B
  A, B = B, r

print(A)
print(int(addAB / A))