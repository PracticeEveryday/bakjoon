import sys

N = int(sys.stdin.readline())

coordinate = []

for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  coordinate.append((x, y))


coordinate.sort()

for i in coordinate:
  print(*i)