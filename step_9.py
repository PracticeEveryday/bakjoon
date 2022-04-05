# num = int(input())

# def recursion(num):
#   if num == 0 :
#     return 1 
#   return num * recursion(num-1)
# print(recursion(num))

num = int(input())

def fibonacci(num) :
  if num == 0:
    return 0  
  elif num == 1 :
    return 1
  else:
    return fibonacci(num-2)+ fibonacci(num-1)
print(fibonacci(num))
