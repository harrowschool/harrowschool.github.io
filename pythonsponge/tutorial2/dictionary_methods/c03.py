x_squared = {x: x**2 for x in range(-10, 11)}
print(x_squared)
phones = dict([('Marco', '7700 900077'), ('Camille', '7700 900338'), ('Manuel', '7700 900439'), ('Ari', '7700 900932')])
print(phones["Marco"])

positional_arguments = ["one", "two", "three", "go"]
keyword_arguments = {"sep": ", ", "end": "\n!", "flush": True}
print(*positional_arguments, **keyword_arguments)
