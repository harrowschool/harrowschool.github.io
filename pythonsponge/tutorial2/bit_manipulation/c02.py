addr = 0b10101100010000111101011010001011

# Keep the least significant byte as-is and convert all other bits as 0s
mask = ___
masked = addr _ mask
print(bin(masked))

# Keep the most significant byte as-is and convert all other bits to 1s
mask = ___
masked = addr _ mask
print(bin(masked))

hex_data = 0x2ef30a54

# Convert the first two bits of each byte to 1s and leave all others as-is
mask = ___
masked = hex_data _ mask
print(hex(masked))
