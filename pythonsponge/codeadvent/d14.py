###########################
# GLOBAL VARIABLES
###########################

total = 0

###########################
# SUBPROGRAMS
###########################


def decode_gss(encoded):
    """Decode a GSS encoded string to its numerical equivalent."""
    # ==> ADD MORE ITEMS TO THE DICTIONARY AS NEEDED
    decode_dict = {'B': '0', 'D': '1', 'F': '2', 'H': '3',
                   'J': '4', 'L': '5', 'N': '6'}
    return int(''.join(decode_dict[ch] for ch in encoded))


def evaluate(expression):
    """Evaluate an RPN expression and return the result."""
    stack = []
    for token in expression.split():
        if token in '+-*':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            # ==> COMPLETE THIS LINE TO HANDLE MULTIPLICATION
            elif 
        else:
            # ==> TRICKY BIT - ADD A LINE HERE TO CONVERT THE TOKEN TO A NUMBER USING THE decode_gss FUNCTION
            
            # ==> AND THEN APPEND THAT TO THE stack LIST

    # the final result is the last item on the stack
    return stack.pop()

###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
DF R HB + *
J NLP - TD +'''.splitlines()

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d14.txt", "r")
# ddata = [line.strip() for line in file.readlines()]
# file.close()

# Evaluate all expressions and sum the results
total = 0
for expr in data:
    # ==> ADD A LINE HERE TO EVALUATE THE EXPRESSION AND ADD THE RESULT TO THE TOTAL

# output the total
print(total)
