pay_change = 1000 - int(input())

coin = 0
# 500 100 50 10 5 1 

while pay_change > 0:
  if pay_change >= 500 :
    pay_change -= 500
    coin += 1
  elif pay_change >= 100 and pay_change < 500:
    pay_change -= 100
    coin += 1
  elif pay_change >= 50 and pay_change < 100 :
    pay_change -= 50
    coin += 1
  elif pay_change >= 10 and pay_change < 50:
    pay_change -= 10
    coin += 1
  elif pay_change >= 5 and pay_change < 10 :
    pay_change -= 5
    coin += 1
  elif pay_change > 0 and pay_change < 10 :
    pay_change -= 1
    coin += 1

print(coin)


'''
N = int(input())
coins = [500, 100, 50, 10, 5, 1]

rest = 1000 - N
result = 0

for coin in coins:
    result += rest // coin
    코인을 나눈 몫을 더해주고
    rest = rest % coin
    코인을 나눈 나머지만 남겨준다.

print(result)
...... 짧다...

'''