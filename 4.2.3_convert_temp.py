user_input = input("please enter a temperture in Celsius to convert to Farenheit: ")
tempc_removec = user_input[0:-1]
tempc_removec_float = float(tempc_removec)
print(tempc_removec_float)

tempF = 1.8 * tempc_removec_float + 32
print(tempF,F)
