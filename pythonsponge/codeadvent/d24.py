###########################
# CONSTANTS
###########################

BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."

###########################
# GLOBAL VARIABLES
###########################

data = ""

###########################
# SUBPROGRAMS
###########################


def xor_process(plaintext, KEY):
    """Encrypts or decrypts a message using XOR encryption."""
    result = ""

    # Convert the key to binary and pad to make its length a multiple of 6
    binary_key = format(KEY, 'b').zfill(6 * ((KEY.bit_length() + 5) // 6))

    # Perform XOR operation between each character of the plaintext and the key
    pos = 0
    for char in plaintext:
        idx = BASE64_ALPHABET.index(char)
        val = int(binary_key[pos:pos+6], 2)
        result += BASE64_ALPHABET[val ^ idx]
        pos = (pos + 6) % len(binary_key)

    return result


###########################
# MAIN PROGRAM
###########################

file = open("d24.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

# Example usage

message = "Christmas is coming."

# a demonstration of the encryption used using INCORRECT a, b and c values
encrypted_message = xor_process(message, 654634324 * 451 * 779791)
print(encrypted_message)
