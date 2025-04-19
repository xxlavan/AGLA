import sympy as sp

def find_eigen(matrix):
    A = sp.Matrix(matrix)
    eigen_data = A.eigenvects()
    return eigen_data

if __name__ == '__main__':
    matrix = [
        [2, 0, 0],
        [0, 3, 4],
        [0, 4, 9]
    ]
    print("Eigenvalues and Eigenvectors:")
    for val, mult, vects in find_eigen(matrix):
        print(f"\nEigenvalue: {val}")
        print(f"Multiplicity: {mult}")
        print("Eigenvectors:")
        for v in vects:
            print(list(v))