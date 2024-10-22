#comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(9, 4, 20))

print(max(2,83,954,89))
def match(str1, str2):
    if str1 == str2:
        print("the strings match")
    else:
        print("the strings don't match")

match("SHABAN", "shaban")