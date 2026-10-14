hour, minute = map(int, input().split())

if hour >= 12:
    ampm = "PM"
    if hour >= 13:
        hour = hour - 12

else:
    ampm = "AM"

if hour < 10:
    hour = "0" + str(hour)

if minute < 10:
    minute = "0" + str(minute)

print(str(hour) + " : " + str(minute) + " " + ampm)
