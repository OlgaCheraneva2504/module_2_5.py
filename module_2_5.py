def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    print(matrix)
get_matrix(2, 3, 15)
get_matrix(0, 7, 2)
get_matrix(6, 5, 135)





