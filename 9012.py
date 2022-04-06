import sys
N = int(sys.stdin.readline())

for i in range(N) :
  stack = []
  bracket = sys.stdin.readline()
  for j in bracket:
    if j == "(":
      stack.append("(")
    elif j == ")" :
      if len(stack) == 0 :
        stack.append(")")
      elif stack[-1] == "(":
        stack.pop()
  if len(stack) == 0 :
    print("YES")
  else :
    print("NO")


# a = [1, 2, 3,]
# print(a[-1])