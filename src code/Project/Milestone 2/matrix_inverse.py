import numpy as np

def find_inverse(matrix, decimal_places=2):
    matrix_size = len(matrix)
    identity_matrix = np.identity(matrix_size).tolist()
    augmented_matrix = [row[:] for row in matrix]  # Copy of matrix

    # Augment matrix with the identity matrix
    for row_index in range(matrix_size):
        augmented_matrix[row_index] += identity_matrix[row_index]

    # Perform Gaussian elimination on the augmented matrix
    for pivot_row in range(matrix_size):
        for row_index in range(pivot_row, matrix_size):
            if abs(augmented_matrix[row_index][pivot_row]) > abs(augmented_matrix[pivot_row][pivot_row]):
                augmented_matrix[pivot_row], augmented_matrix[row_index] = augmented_matrix[row_index], augmented_matrix[pivot_row]
        for target_row in range(pivot_row + 1, matrix_size):
            elimination_factor = augmented_matrix[target_row][pivot_row] / augmented_matrix[pivot_row][pivot_row]
            for column_index in range(2 * matrix_size):
                augmented_matrix[target_row][column_index] -= elimination_factor * augmented_matrix[pivot_row][column_index]

    # Back substitution to form the inverse matrix
    for pivot_row in range(matrix_size - 1, -1, -1):
        for row_index in range(pivot_row):
            elimination_factor = augmented_matrix[row_index][pivot_row] / augmented_matrix[pivot_row][pivot_row]
            for column_index in range(2 * matrix_size):
                augmented_matrix[row_index][column_index] -= elimination_factor * augmented_matrix[pivot_row][column_index]
        divisor = augmented_matrix[pivot_row][pivot_row]
        for column_index in range(2 * matrix_size):
            augmented_matrix[pivot_row][column_index] /= divisor

    inverse_matrix = [row[matrix_size:] for row in augmented_matrix]

    # Round the inverse matrix to the specified number of decimal places
    inverse_matrix = [[round(value, decimal_places) for value in row] for row in inverse_matrix]

    return inverse_matrix
