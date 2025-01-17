###########################
# GLOBAL VARIABLES
###########################

data = ""
nums = []

###########################
# SUBPROGRAMS
###########################


def to_7_bit_binary(num):
    """Convert a positive integer to its 7-bit binary representation."""
    binary = ''
    for _ in range(7):
        binary = str(num % 2) + binary
        num = num // 2
    return binary


def to_twos_complement(num_string):
    """Convert an integer to its 8-bit two's complement binary representation."""
    num = int(num_string)  # Convert the string to an integer

    if num >= 0:
        # ==> IF POSITIVE PREPEND 0 TO A CALL TO GET THE 7-BIT FORM
        return '0' + _____________________
    else:
        # For negative numbers, prepend '1' to the 7-bit binary form of the positive counterpart
        positive_counterpart = 128 + num  # This will be a positive number
        # ==> IF NEGATIVE PREPEND 1 TO A CALL TO GET THE 7-BIT FORM OF ITS POSITIVE COUNTERPART
        return '1' + _____________________


def create_summary_number(numbers):
    """Create a summary binary number from a list of integers."""
    summary_bits = []
    # ==> COMPLETE THE TWO GAPS BELOW
    for i, num_string in enumerate(_______):
        binary = to_twos_complement(_________)
        bit_index = i % 8
        # ==> ADD THE CORRECT BIT TO THE summary_bits LIST

    return ''.join(summary_bits)

###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
3
-5
127
-128'''.splitlines()

# uncomment these two lines to use the real challenge data instead when ready
# with open("data.txt", "r") as datafile:
#     data = [line.strip() for line in datafile.readlines()]

# Find the summary binary sequence
print(create_summary_number(data))
