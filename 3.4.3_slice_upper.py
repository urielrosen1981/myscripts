userinput = input("please enter your string: ")
charnumber = len(userinput)
halfstringvalue = charnumber // 2
print(halfstringvalue)
firsthalf = userinput[0:halfstringvalue]
secondhalf = userinput[halfstringvalue:]
print(firsthalf)
newstring = secondhalf.upper()
print(firsthalf + newstring)