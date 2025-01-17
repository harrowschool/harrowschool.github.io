to_encrypt = "Attack at dawn"
print("Encrypting:", to_encrypt)
# Returns a number like 0x48656c6c6f20776f726c6421
as_number = int.from_bytes(bytes(to_encrypt, 'ascii'), 'big')

# Don't change this line
one_time_pad = 0x7059279455aac686cae065ad9d68

encrypted = ___ _ ___
print("Encrypted text:", hex(encrypted))

decrypted_as_number = ___ _ ___
decrypted = str(decrypted_as_number.to_bytes(len(to_encrypt), 'big'), 'ascii')
print("Decrypted text:", decrypted)
