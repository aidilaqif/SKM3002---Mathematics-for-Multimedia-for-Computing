def gaussian_elimination(coefficient_matrix, constants_vector, decimal_places=2):
    number_of_equations = len(constants_vector)
    augmented_matrix = [row[:] for row in coefficient_matrix]

    # Augmenting the matrix coefficient_matrix with vector constants_vector
    for row_index in range(number_of_equations):
        augmented_matrix[row_index].append(constants_vector[row_index])

    # Forward elimination
    for pivot_row in range(number_of_equations):
        # Make the pivot_row-th row's pivot_row-th element 1
        for row_index in range(pivot_row, number_of_equations):
            if abs(augmented_matrix[row_index][pivot_row]) > abs(augmented_matrix[pivot_row][pivot_row]):
                augmented_matrix[pivot_row], augmented_matrix[row_index] = augmented_matrix[row_index], augmented_matrix[pivot_row]
        for target_row in range(pivot_row + 1, number_of_equations):
            elimination_factor = augmented_matrix[target_row][pivot_row] / augmented_matrix[pivot_row][pivot_row]
            for column_index in range(pivot_row, number_of_equations + 1):
                augmented_matrix[target_row][column_index] -= elimination_factor * augmented_matrix[pivot_row][column_index]

    # Check for inconsistent rows
    for row in augmented_matrix:
        if all(abs(x) < 1e-9 for x in row[:-1]) and abs(row[-1]) > 1e-9:  # All coefficients are zero but the constant is non-zero
            return None  # Indicate no solution

    # Back substitution
    solution_vector = [0 for _ in range(number_of_equations)]
    solution_vector[number_of_equations - 1] = augmented_matrix[number_of_equations - 1][number_of_equations] / augmented_matrix[number_of_equations - 1][number_of_equations - 1]
    for row_index in range(number_of_equations - 2, -1, -1):
        sum_ax = 0
        for column_index in range(row_index + 1, number_of_equations):
            sum_ax += augmented_matrix[row_index][column_index] * solution_vector[column_index]
        solution_vector[row_index] = (augmented_matrix[row_index][number_of_equations] - sum_ax) / augmented_matrix[row_index][row_index]

    # Round the solution vector to the specified number of decimal places
    solution_vector = [round(value, decimal_places) for value in solution_vector]

    return solution_vector
