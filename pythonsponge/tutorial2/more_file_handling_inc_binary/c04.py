data = []

# reading four bytes per number, little-endian
with open("data2.bin", "rb") as myfile:

    while True:

        # ==> COMPLETE THE NEXT LINE
        bytes = myfile.read(_)
        if bytes == b"":
            break

        # ==> COMPLETE THE NEXT LINE
        value = int.from_bytes(_____, "______", signed=____)
        data.append(value)

# ==> CALCULATE AND OUTPUT THE PRODUCT (MULTIPLICATION) OF THE TWO VALUES
