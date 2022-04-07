N = int(input())

ATM_duration = list(map(int, input().split()))

ATM_duration.sort()

time = []
for i in range(1, len(ATM_duration)+1):
  time.append(sum(ATM_duration[:i]))

print(sum(time))