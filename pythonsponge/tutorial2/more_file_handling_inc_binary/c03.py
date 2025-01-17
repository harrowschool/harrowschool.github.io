with open("data.bin", "rb") as myfile:
  data = list(myfile.read())

print("Bytes read:", data)
print("Total of stored bytes:", sum(data))

print("or perhaps these bytes should be interpreted as ....")

# Now interpreting as two bytes per number, big-endian
data = []
with open("data.bin", "rb") as myfile:
    while True:
        bytes = myfile.read(2)
        if bytes == b"":
          break
        value = int.from_bytes(bytes, "big", signed=False)
        data.append(value)

print(data)

print("or perhaps as ....")

# Now interpreting as two bytes per number, little-endian
data = []
with open("data.bin", "rb") as myfile:
    while True:
        bytes = myfile.read(2)
        if bytes == b"":
          break
        value = int.from_bytes(bytes, "little", signed=False)
        data.append(value)

print(data)