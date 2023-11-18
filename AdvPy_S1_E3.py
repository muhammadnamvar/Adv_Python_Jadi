header = ['Name', 'Genre1', 'Genre2', 'Genre3']
data = []
n = int(input("please enter number of people: "))
for i in range(n):
    row = []
    name = input("please enter your name: ")
    row.append(name)
    for j in range(3):
        genre = input("please enter your genre: ")
        row.append(genre)
    data.append(row)


dct = {}
for row in data:
    for genre in row[1:]:
        if genre not in dct:
            dct.update({genre: 1})
        else:
            dct.update({genre: dct[genre]+1})

for keys, value in dct.items():
    print(keys, value)

