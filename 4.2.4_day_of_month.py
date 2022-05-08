import calendar
import datetime

inputdate = input("Please enter the date and find the day: ")

DD=inputdate[:2]
MM=inputdate[3:5]
YY=inputdate[6:10]
MMnew=int(MM) # changed line
DDnew=int(DD) # changed line
YYnew=int(YY) # changed line
print (YYnew ,MMnew, DDnew )
#print(calendar.weekday(YYnew,MMnew,DDnew)) # prints out 2
#weekday(YYnew, MMnew, DDnew)
day = calendar.weekday(YYnew, MMnew, DDnew)
if day == 0:
    print("Monday")
elif day == 1:
    print("Tuesday")
elif day == 2:
    print("Wednesday")
elif day == 3:
    print ("Thursday")
elif day == 4:
    print ("Friday")
elif day == 5:
    print ("Saturday")
elif day == 6:
    print ("Sunday")
else : 
    print ("error")
