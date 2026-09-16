# Assignment 4
# Question 10 : Time Conversion

totalSeconds = int(input("Enter total seconds : "))

hours = totalSeconds//3600
remaining_seconds = totalSeconds - hours*3600

minutes = remaining_seconds // 60
seconds = remaining_seconds - minutes*60

print("Hours =", (hours))
print("Minutes =",(minutes))
print("Seconds =",(seconds))