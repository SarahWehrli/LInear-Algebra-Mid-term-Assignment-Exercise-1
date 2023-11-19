def main():
    # Exercise c, 10 provided sample square matrices for testing
    matrices = [
        [[1, 0, 1], [0, 1, 2], [6, 9, 1]],
        [[3, 2, 6], [4, 5, 8], [2, 8, 9]],
        [[2, 2, 9], [4, 4, 14], [1, 0, 3]],
        [[1, 2, 2], [0, 5, 4], [5, 6, 1]],
        [[2, 1, 3], [4, 2, 6], [8, 4, 12]],
        [[2, 0, 0], [0, 3, 0], [0, 0, 4]],
        [[1, 2, 3], [5, 6, 7], [9, 10, 11]],
        [[1, 2, 0], [0, 5, 6], [8, 0, 9]],
        [[1, 0, 2], [0, 0, 0], [4, 0, 5]],
        [[1, 1, 0], [1, 2, 1], [0, 1, 3]]]

    # Run the program for all the provided matrices and calcualte the inverse if possible
    for matrix in matrices:
        try:
            matrix_inversed = inverse(matrix)
            print("Inverse Matrix:")
            for row in matrix_inversed:
                print(row)
        except ValueError:
            print("This matrix is singular. Hence the matrix is not invertible.")


    # Exercise d, asking the user for the input for the system of equations
    try:
        A = eval(input("Enter the left side of the equation as a matrix as a list of lists: ")) # using eval so pythons knows it is handled as a list with strings, I found this function on the following Website: https://www.w3schools.com/python/ref_func_eval.asp called: 17.11.2023
        b = eval(input("Enter the vector b on the right of the equation as a list: "))
        solution_linear_equation = solve_linear_equation(A, b)
        print("The solution for the system of linear equations is: ")
        print(solution_linear_equation)
    except ValueError:
        print("Cannot solve the system of linear equations because it has either more than one solution or no solutions: ")


# Calculates the inverse of a matrix with Gauss Algorithm
def inverse(matrix):
    # Check if the matrix is invertible
    # If the matrix isn't a square matrix or the determinant is zero, it raises an Error
    if len(matrix) != len(matrix[0]) or calculate_determinant(matrix) == 0:
        raise ValueError("This matrix is singular. Hence the matrix is not invertible.")

    # Find the the size of the matrix by the number of rows
    n = len(matrix)

    # Create an identity matrix of the same size as the provided matrix to create the right side of the gauss elimination
    identity_matrix = [[0] * n for k in range(n)] # creating a null matrix with the size of nxn
    for r in range(n):
        identity_matrix[r][r] = 1 # changes the diagonal zeros to 1 

    # Gaussian elimination to create the identity matrix starts here using pivotization for a fast solution inspired by this online inverse calculator: https://matrix.reshish.com/de/inverCalculation.php called: 17.11.2023
    # 1. Step
    for col in range(n): # iterate over the columns 
        # find the pivot elements (diagonals)
        pivot = matrix[col][col]
       
        # 2. Step
        # in general dividing the current row by the pivot provided in step 1 and doing the same with the identity matrix
        try:
            for p in range(n): # iterating over each column
                matrix[col][p] /= pivot
                identity_matrix[col][p] /= pivot
        except ZeroDivisionError: # raises an Error if there is an attempt of a ZeroDivision
            print("This matrix is singular. Hence the matrix is not invertible.")

        # 3. Step
        # Subtract multiples of the current row from the other rows to make their elements 0
        for r in range(n): # iterating over each rows
            if r != col: # make sure the current row is not the same as the pivot row
                factor = matrix[r][col] # determine the factor for the scaling befor subtracting the rows
                for j in range(n):
                    matrix[r][j] -= factor * matrix[col][j] # multiplying the current pivot and subtracting it from the other row
                    identity_matrix[r][j] -= factor * identity_matrix[col][j] # doing the same with the identity matrix to get the inverse

    return identity_matrix


# Calculate Determinant of a 3x3 matrix to check if the matrix is invertible
def calculate_determinant(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g) # Formula to calculate the determinant 
    return determinant


# Solve the system of linear equations Ax = b 
def solve_linear_equation(A, b):
    try:
        A_inverted = inverse(A) # calls the function inverse to calculate the inverse of A
        x = matrix_vector_multiply(A_inverted, b) # calls the function matrix_vector_multiply using the inverse of A and the vector b
        return x # returns the calculated solution
    except ValueError:
        raise ValueError("Cannot solve the system of linear equations because it has either more than one solution or no solutions: ")
    

# Multiply a matrix by a vector using this formula A^-1 * b = x
def matrix_vector_multiply(matrix, vector):
    multiplication = [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))] # using listcomprehensenmethod with help from the following website: https://hashdork.com/de/matrix-multiplication-in-python-without-numpy/ called: 17.11.2023
    return multiplication

if __name__ == "__main__":
    main()
