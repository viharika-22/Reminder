import datetime
import time
from plyer import notification
if __name__ =="__main__":
    alarmHour= int(input("Hour: "))
    alarmMinute=int(input("Minute: "))
    amPm= str(input("am or pm"))
    if(amPm=="pm" and alarmHour!=12):
        alarmHour= alarmHour+12
    while(True):
        if(alarmHour==datetime.datetime.now().hour and alarmMinute== datetime.datetime.now().minute):
            notification.notify(
            title = "*Work",
            message= "Study",
            timeout=10
            #app_icon=
            )
            break
