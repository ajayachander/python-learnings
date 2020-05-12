hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
dura_hour = int(dura/60)
dura_mins = dura % 60
print(dura_hour,dura_mins)
ext_hour = int ((mins + dura_mins)/60)
end_hour = (((hour + dura_hour) % 24) + ext_hour)
end_mins = (mins + dura_mins) % 60
print("The End-Time is",end_hour,":",end_mins)
