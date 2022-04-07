number = input()

number_list = list(number)

number_list.sort(reverse=True)

print(int("".join( number_list)))