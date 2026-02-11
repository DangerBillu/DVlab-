import pandas as pd
data = {
    "roll number": [1,2,3,4,5,6,7,8,9,10], 
    "name": ["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"],
    "gender": ["m", "f", "m", "f","m", "f", "m", "f", "m", "f" ],
    "marks1": [80, 31, 82, 43, 84, 65, 86, 87, 22, 89], 
    "marks2": [39, 83, 36, 85, 87, 83, 12, 95, 50, 79], 
    "marks3": [68, 20, 62, 54, 76, 78, 80, 72, 84, 46], 
}
df= pd.DataFrame(data)
print(df)

df["total"]= df["marks1"]+df["marks2"]
print("with total marks:\n", df)

print("lowest marks on marks1:\n", df["marks1"].min())
print("highest marks on marks2:\n", df["marks2"].max())
print("average marks on marks3:\n", df["marks3"].mean())

df["average"]= (df["total"])/3
print("student with highest marks:\n", df.loc[df["average"].idxmax(), "name"])

count = (df["marks2"]<40).sum()
print("the count of failed students is:\n", count)
