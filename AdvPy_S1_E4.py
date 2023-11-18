import pandas as pd


n = int(input("Please enter the number of programmer: "))
names = []
for i in range(n):
    pgr = input(f"Please enter {i+1}'s programmer info: ")
    row = pgr.split(".")
    names.append(row)


for i in range(n):
    for j in range(3):
        names[i][j] = names[i][j].capitalize()
names.sort()


# creating df object with columns specified(For Pretty Print)
df = pd.DataFrame(names, columns=['Gender', 'name', 'Language'])
print(df.to_string(index=False))
