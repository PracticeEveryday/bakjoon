# import sys

# N = int(sys.stdin.readline())

# meeting_room = []

# for i in range(N):
#   start_time, end_time = map(int, sys.stdin.readline().split())
#   meeting_room.append((start_time, end_time))
# meeting_room.sort()
# print(meeting_room)

# min_y = [(x, y) for x, y in meeting_room if y == min([y for  x, y in meeting_room])][0]
# target = []
# for i in range(len(meeting_room)):
#   if meeting_room[i][0] <= min_y[1] and meeting_room[i][0] > min_y[0]: 
#     target.append(meeting_room[i])

# print(min_y)
# print(target)


import sys

N = int(sys.stdin.readline())

meeting_room = []

for i in range(N):
  start_time, end_time = map(int, sys.stdin.readline().split())
  meeting_room.append((start_time, end_time))
# print(meeting_room)

meeting_room = sorted(meeting_room, key=lambda x : x[0])
meeting_room = sorted(meeting_room, key=lambda x : x[1])
# print(meeting_room)

y_value = 0
result = []
for x, y in meeting_room:
  if x >= y_value :
    result.append((x,y))
    y_value = y

print(len(result))