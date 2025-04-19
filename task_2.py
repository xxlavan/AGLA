def inverse_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        print("The matrix must be square to compute its inverse.")
        return

    n = [row + [1 if i == j else 0 for j in range(len(matrix))] for i, row in enumerate(matrix)]

    for i in range(len(n)):
        divide = n[i][i]
        for v in range(len(n) * 2):
            n[i][v] = n[i][v] / divide

        for j in range(i + 1, len(n)):
            if n[i][i] == 0:
                break
            subtraction = n[j][i] / n[i][i]
            for z in range(len(n) * 2):
                n[j][z] -= subtraction * n[i][z]

    for i in range(len(n) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if n[i][i] == 0:
                break
            subtraction = n[j][i] / n[i][i]
            for z in range(len(n) * 2):
                n[j][z] -= subtraction * n[i][z]

    inverse = [row[len(matrix):] for row in n]

    return inverse
#Enter matrix
matrix = [
    [_, _],
    [_, _]
]

inverse = inverse_matrix(matrix)

for row in inverse:
    print(row)
