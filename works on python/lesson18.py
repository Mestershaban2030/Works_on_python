#while loop
i = 1
while i<=10:
    print(i)
    i += 1
else:
    print("the condition not true")
print("the loop has ended")
##################################################
i = 1
while i <= 10:
    i += 1
    if i == 6:
        continue
    print(i)

print("the loop has ended")

####################################################
i = 1
while i <= 10:
    i += 1
    if i == 6:
       break
    print(i)

print("the loop has ended")