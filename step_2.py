# a, b = map(int, input().split())

# if a > b :
#   print(">")
# elif a < b:
#   print("<")
# else : 
#   print("==")

# score = int(input())

# if score <=100 and score >=90:
#   print("A")
# elif score < 90 and score >=80:
#   print("B")
# elif score <80 and score >=70:
#   print("C")
# elif score <70 and score >=60:
#   print("D")
# else : 
#   print("F")

# year = int(input())

# if (year%4==0 and year%100 != 0) or year%400 == 0:
#   print(1)
# else :
#   print(0)

# a = int(input())
# b = int(input())

# if a > 0 and b > 0 :
#   print(1)
# elif a < 0 and b < 0 :
#   print(3)
# elif a < 0 and b > 0 :
#   print(2)
# else :
#   print(4)

# a, b = map(int, input().split())

# if(b-45 < 0) :
#   if a == 0 :
#     a = 24
#   a = a - 1
#   b = 60 - (45 - b)
#   print(a, b)
# else :
#   print(a, b-45)

# hour, minute = map(int, input().split())
# duration = int(input())

# if duration >= 60 :
#   duration_hour = int(duration / 60)
#   duration_minute = duration % 60

#   if duration_minute + minute >= 60 :
#     hour = hour + 1
#     if hour + duration_hour > 23:
#       print(hour + duration_hour - 24, minute + duration_minute - 60)
#     else :
#       print(hour + duration_hour, minute + duration_minute - 60)
#   else :
#     print(hour, minute + duration_minute)
# else :
#   duration_minute = duration
#   if duration_minute + minute >= 60 :
#     hour = hour + 1
#     if hour > 23:
#       hour = hour - 24
#       print(hour, minute + duration_minute - 60)
#     else :
#       print(hour, minute + duration_minute - 60)
#   else:
#     print(hour, minute + duration_minute)

a, b, c = map(int, input().split())

if a == b == c :
  print(a*1000 + 10000)
elif a == b or a == c or b == c :
  if a == b:
    print(a*100 +1000)
  elif b == c:
    print(b*100 +1000)
  else :
    print(c*100 +1000)    
else : 
  lst = [a, b, c]
  lst.sort()
  print(lst[2]*100)


