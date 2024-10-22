# condition
is_hungry = True
want_to_eat=False
if is_hungry or want_to_eat:
    print("go eat")
else:
    print("Sleep")

if is_hungry and want_to_eat:
    print("go eat")
elif is_hungry and not want_to_eat:
    print("die")
else:
    print("Sleep")
