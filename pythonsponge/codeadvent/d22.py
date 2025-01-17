###########################
# GLOBAL VARIABLES
###########################

data = []

###########################
# SUBPROGRAMS
###########################


def solve_linear_equations(pData):
    # Split the input data into lines and then into coefficients and constants
    equations = [line.split('|') for line in pData]
    coefficients = [[int(num) for num in equation[0].split()]
                    for equation in equations]
    constants = [int(equation[1]) for equation in equations]

    # Gaussian elimination
    for i in range(len(coefficients)):

        # Scale the first row to make the diagonal element non-zero and largest
        if coefficients[i][i] == 0:
            for j in range(i + 1, len(coefficients)):
                if coefficients[j][i] != 0:
                    coefficients[i], coefficients[j] = coefficients[j], coefficients[i]
                    constants[i], constants[j] = constants[j], constants[i]
                    break

        for j in range(i + 1, len(coefficients)):

            if coefficients[j][i] % coefficients[i][i] != 0:
                # scale up the row to make the element an integer
                for k in range(i, len(coefficients[j])):
                    coefficients[j][k] *= coefficients[i][i]
                constants[j] *= coefficients[i][i]

            scale_factor = coefficients[j][i] // coefficients[i][i]

            for k in range(i, len(coefficients[j])):
                coefficients[j][k] -= scale_factor * coefficients[i][k]
            constants[j] -= scale_factor * constants[i]

    # Back substitution
    solution = [0] * len(coefficients)
    for i in range(len(coefficients) - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, len(coefficients)):
            solution[i] -= coefficients[i][j] * solution[j]
        solution[i] /= coefficients[i][i]

    return solution

###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
2 3 7 | 29
3 2 1 | 10
5 1 4 | 19'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d22.txt", "r")
# data = [line.strip() for line in file.readlines()]
# file.close()

# Solve the system of linear equations
print(solve_linear_equations(data))
