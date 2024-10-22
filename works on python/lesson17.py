#Dictionaries
convert_month={
    "5":True,
    "feb":"febraury",
    "mar":"marth"
}
print(convert_month["mar"])
print(convert_month.get("5"))#give defult falut "none"
print(convert_month.get("febee","Sahaban Soltaan"))

