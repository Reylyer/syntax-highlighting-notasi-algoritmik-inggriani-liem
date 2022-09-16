nbkol = 3
nbbar = 4
asd = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
]
X = 6
i = 0

while asd[i//nbkol][i%nbkol] != X and i < nbkol * nbbar:
    print(i//nbkol, i%nbkol)
    i += 1
x = i//nbkol
y = i%nbkol
