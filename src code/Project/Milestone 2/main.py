from gaussian_elimination import gaussian_elimination
from matrix_inverse import find_inverse

def get_matrix_input(rows, prompt):
    # Get matrix input from the user.
    matrix = []
    print(prompt)
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"  Enter row {i + 1} (space-separated numbers): ").split()))
                if len(row) != rows:
                    raise ValueError(f"Each row must have {rows} elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
                print("  Please enter the row again.")
    return matrix

def get_vector_input(length, prompt):
    # Get vector input from the user.
    while True:
        try:
            vector = list(map(float, input(prompt).split()))
            if len(vector) != length:
                raise ValueError(f"The vector must have {length} elements.")
            return vector
        except ValueError as e:
            print(e)
            print("  Please enter the vector again.")

def main():
    print("\nWelcome to the Linear Algebra Solver!")
    print("This program can solve a system of linear equations or find the inverse of a matrix.\n")
    choice = input("Choose an option:\n1. Solve a system of linear equations\n2. Find the inverse of a matrix\nEnter 1 or 2: ")
    print()

    if choice == '1':
        while True:
            try:
                number_of_variables = int(input("Enter the number of variables: "))
                if number_of_variables <= 0:
                    raise ValueError("The number of variables must be a positive integer.")
                break
            except ValueError as e:
                print(e)
                print("Please enter a valid number of variables.\n")

        coefficient_matrix = get_matrix_input(number_of_variables, "\nEnter the coefficient matrix A:")
        print()
        constants_vector = get_vector_input(number_of_variables, "Enter the constants vector b (space-separated numbers): ")
        print()
        solution = gaussian_elimination(coefficient_matrix, constants_vector)
        if solution is None:
            print("The system of linear equations has no solution.\n")
        else:
            print("Solution vector x is:\n")
            for value in solution:
                print(f"  {value}")
            print()

    elif choice == '2':
        while True:
            try:
                matrix_size = int(input("Enter the size of the matrix (n x n): "))
                if matrix_size <= 0:
                    raise ValueError("The size of the matrix must be a positive integer.")
                break
            except ValueError as e:
                print(e)
                print("Please enter a valid size for the matrix.\n")

        matrix = get_matrix_input(matrix_size, "\nEnter the matrix A:")
        print()
        inverse_matrix = find_inverse(matrix)
        print("Inverse of matrix A is:\n")
        for row in inverse_matrix:
            print("  ", row)
        print()
    else:
        print("Invalid choice. Please restart the program and enter 1 or 2.\n")

if __name__ == "__main__":
    main()
