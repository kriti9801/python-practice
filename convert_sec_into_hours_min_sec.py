#convert seconds intto hours,minutes,and seconds
total_seconds = int(input("enter totalseconds:"))
hours = total_seconds // 3600
remaining_seconds = total_seconds%3600
minutes = remaining_seconds//60
seconds = remaining_seconds%60
print("Hours=",hours)
print("minutes=",minutes)
print("Seconds=",seconds)
