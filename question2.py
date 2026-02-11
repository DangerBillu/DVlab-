import pandas as pd

temps= [29, 30, 25, 26, 24, 27, 28]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data = pd.Series(temps, index = days)
print("tempratures:\n", data)

avgtemp = data.mean()
print("average temprature:\n", avgtemp)

print("maximum temprature:\n", data.max(), "on", data.idxmax())
print("minimum tempratures:\n", data.min(), "on", data.idxmin())

print("tempratures above 28 degrees:\n", data[data>28])

farenheit= (data* 9/5)+32
print("temprature is farenheit:\n", farenheit)

print ("days with temprature above avg:\n" , data[data>avgtemp])
