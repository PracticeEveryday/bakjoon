import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
  action = sys.stdin.readline()
  action_list = action.split()
  if action_list[0] == "push":
    stack.append(action_list[1])
  elif action_list[0] == "top":
    if len(stack) == 0:
      print(-1)
    else :
      print(stack[-1])
  elif action_list[0] == "pop":
    if len(stack) == 0:
      print(-1)
    else :
      print(stack.pop())
  elif action_list[0] == "size":
    print(len(stack))
  elif action_list[0] == "empty":
    if len(stack) == 0:
      print(1)
    else : 
      print(0)

