import time
print("enter ' H ' for inputing time in hours")
print("enter ' M ' for inputing time in minutes")
print("enter ' S ' for inputing time in seconds")

print("********************************************")

mytime=int(input("enter the time in seconds"))
for x in reversed(range(1,mytime)):
    seconds=x%60
    minutes=int(x/60)%60
    hour=int(x/3600)
    time.sleep(1)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")

    print("TIMES UP!!")