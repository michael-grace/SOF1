#***Sparse Matrices***

def sparse_dimension(sparse_matrix):
    x_coords = []
    y_coords = []
    for coord in sparse_matrix.keys():
        x_coords.append(coord[0])
        y_coords.append(coord[1])
    return (max(x_coords), max(y_coords))

def sparse_addition(matrix_a, matrix_b):
    for point in matrix_b.keys():
        if point in matrix_a.keys():
            matrix_a[point] += matrix_b[point]
        else:
            matrix_a[point] = matrix_b[point]
    return matrix_a

def sparse_transpose(sparse_matrix):
    transpose = {}
    for point in sparse_matrix.keys():
        transpose[(point[1], point[0])] = sparse_matrix[point]
    return transpose

lilians_matrix = {
    (3,1): 2,
    (2,2): 1,
    (4,2): 1,
    (5,4): 1,
    (1,5): 4,
    (6,6): 2
}

print(sparse_dimension(lilians_matrix))
print(sparse_transpose(lilians_matrix))

    