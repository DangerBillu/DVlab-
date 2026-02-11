import pandas as pd

steps= [3000, 4000, 5000, 6000, 7000, 8000, 9000]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

data = pd.Series(steps, index=days)
print("Steps walked each day:\n", data)

totalsteps = data.sum()
print("total steps walked in the week:", totalsteps)

print("highest steps:\n", data.max(), "on", data.idxmax())
print("lowest steps:\n", data.min(), "on", data.idxmin())

print("days with more than 8000 steps:\n", data[data>8000])

km = data/1250
print("Steps converted to kilometers:\n", km)

avgsteps = data.mean()
print("days with above avg steps:\n", data[data>avgsteps])
