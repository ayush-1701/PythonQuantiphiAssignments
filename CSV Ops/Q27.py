import pandas as pd
import csv
year = 2020
file = open('sample1.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)

df = pd.read_csv("sample1.csv")
df["Year"] = 2020
df.to_csv("sample1.csv", index=False)

for i in rows:
    print(i)

file.close()
