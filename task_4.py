def transpose(M):
    return [list(row) for row in zip(*M)]


def rref(M):
    A = [row[:] for row in M]
    m = len(A)
    n = len(A[0]) if m > 0 else 0
    pivots = []
    row = 0

    for col in range(n):
        sel = None
        for i in range(row, m):
            if A[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        A[row], A[sel] = A[sel], A[row]
        pivot_val = A[row][col]
        A[row] = [x / pivot_val for x in A[row]]
        for i in range(m):
            if i != row and A[i][col] != 0:
                factor = A[i][col]
                A[i] = [A[i][j] - factor * A[row][j] for j in range(n)]
        pivots.append(col)
        row += 1
        if row == m:
            break

    return A, pivots


def column_space(A):
    _, pivots = rref(A)
    AT = transpose(A)
    return [AT[j] for j in pivots]


def row_space(A):
    R, _ = rref(A)
    return [row for row in R if any(x != 0 for x in row)]


def null_space(A):
    R, pivots = rref(A)
    m = len(R)
    n = len(R[0]) if m > 0 else 0
    piv_set = set(pivots)
    free = [j for j in range(n) if j not in piv_set]
    basis = []

    for f in free:
        vec = [0.0] * n
        vec[f] = 1.0
        for i, p in enumerate(pivots):
            vec[p] = -R[i][f]
        basis.append(vec)

    return basis


def orthogonal_complement(A):
    return null_space(transpose(A))


if __name__ == "__main__":
    A = [
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ]

    print("Orthogonal complement of column space:")
    for v in orthogonal_complement(A):
        print(v)
