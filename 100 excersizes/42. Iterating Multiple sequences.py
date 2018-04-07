# print out in each line the sum of homologous items of the two sequences

a = [1, 2, 3]
b = (4, 5, 6)
c = list(b)

for x in zip(a, c):
    print(sum(x))

for i, j in zip(a, b):
    print(i + j)