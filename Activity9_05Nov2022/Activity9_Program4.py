# Python program to multiply two matrices

def matrix_multiplication(matA, matB):
    rowsA = len(matA)
    colsA = len(matA[0])
    rowsB = len(matB)
    colsB = len(matB[0])

    if colsA != rowsB:
        print("Matrix sizes are not compatible!")
        return

    # Define resultant matrix
    matC = []
    for row in range(rowsA):
        curr_row = []
        for col in range(colsA):
            curr_row.append(0)
        matC.append(curr_row)

    # Perform Matrix Multiplication
    for i in range(rowsA):
        for j in range(colsB):
            curr_val = 0
            for k in range(colsA):
                curr_val += matA[i][k] * matB[k][j]
            matC[i][j] = curr_val

    return matC


A = [[2, 2], [2, 2]]
B = [[1, 1], [1, 1]]

print("Resultant Matrix = ", matrix_multiplication(A, B))
