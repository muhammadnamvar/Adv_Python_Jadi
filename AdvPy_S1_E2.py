import pandas as pd


table = []
match1 = input("iran-spain: ")
match2 = input("iran-Portugal: ")
match3 = input("iran-morocco: ")
match4 = input("Portugal-spain: ")
match5 = input("Portugal-morocco: ")
match6 = input("spain-morocco: ")


# Write a "2D list" to CSV
path = "C:/Users/Administrator/PycharmProjects/pythonProject/football_group.csv"
header = ['Name', 'games', 'wins', 'loses', 'draws', 'goal difference', 'points']
data = [['spain', 0, 0, 0, 0, 0, 0],
        ['iran', 0, 0, 0, 0, 0, 0],
        ['morocco', 0, 0, 0, 0, 0, 0],
        ['portugal', 0, 0, 0, 0, 0, 0]]
df = pd.DataFrame(data, columns=header)
df.to_csv(path, index=False)
