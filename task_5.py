def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v.copy()
        for u in basis:
            coeff = dot_product(v, u) / dot_product(u, u)
            w = [wi - coeff * ui for wi, ui in zip(w, u)]
        if any(wi != 0 for wi in w):
            basis.append(w)
    return basis


if __name__ == '__main__':
    vecs1 = [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ]
    print("Orthonormal basis for vecs1:")
    for ortho in gram_schmidt(vecs1):
        print(ortho)
