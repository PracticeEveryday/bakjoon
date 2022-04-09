count, price = map(int, input().split())

value = []
coin = 0
for i in range(count) :
  value.append(int(input()))

value.sort(reverse=True)

while price > 0 :
  for i in value :
    coin += price // i
    price = price % i

print(coin)