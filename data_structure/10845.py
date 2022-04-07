import sys

N = int(sys.stdin.readline())
q = []

for i in range(N):
  action = sys.stdin.readline()
  action_list = action.split()

  if action_list[0] == "push":
    q.append(action_list[1])
  elif action_list[0] == "pop":
    if len(q) == 0 :
      print(-1)
    else : 
      print(q.pop(0))
  elif action_list[0] == "size":
    print(len(q))
  elif action_list[0] == "empty":
    if len(q) == 0:
      print(1)
    else :
      print(0)
  elif action_list[0] == "front":
    if len(q) == 0 :
      print(-1)
    else :
      print(q[0])
  elif action_list[0] == "back":
    if len(q) == 0:
      print(-1)
    else :
      print(q[-1])