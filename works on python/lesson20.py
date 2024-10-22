#loops with if conditions
for char in "ShabanSoltan":
    print(char)
########################################
boddies=["pikachu","grandizer","Shaban"] 
for body in boddies:
    print(body) 
########################################
for x in range(10,20):
    print(x)
#########################################
    boddies=["pikachu","grandizer","Shaban"]
print(len(boddies))
#########################################
string="ShabanSoltan"
for index in range(len(string)):
    print(index)
#########################################
    boddies = ["pikachu", "grandizer", "Shaban"]
for index in range(len(boddies)):
    print(boddies[index])
#########################################
boddies = ["pikachu", "grandizer", "Shaban"]
for bodddies in range(10):
    if index%2==0:
        print(index,"Is an even num")
    else:
        print(index,"Is an odd num")    
#########################################
boddies = ["pikachu", "grandizer", "Shaban","Winner"]
for boddy in range(len(boddies)):
    if boddies[boddy] == "Winner":
        print(boddy, "Is The Winner")
    else:
        print(boddy, "Is not The Winner")
###########################################
boddies = ["pikachu", "grandizer", "Shaban","Winner"]
for body in bodddies:
    if body=="Shaban":
        print(body,"Is Your Friend")
        break
    else:
        print(body,"Is not a frind")
