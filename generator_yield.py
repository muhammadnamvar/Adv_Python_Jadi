def firstn(n):
    i = 0
    while i <= n:
        yield i
        i += 1


for num in firstn(500):
    print(num)
