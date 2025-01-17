#################
# LIBRARY IMPORTS
#################

from imagelib import load_package
from imagelib import load_image
from math import floor

###############
# CONSTANTS
###############

# ASCII characters to use for the conversion
# Ensure these characters are arranged from smaller to larger characters to match white to black on the greyscale
# ==> EXTENSION: Experiment with different character sets
ASCII = " .:-=+*%#@"

# Only certain sites which allow cross-origin requests will allow us to pull images directly
IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQngA3sDiSoA46Dy56OLZjLKD1SqgsS3Qmh1A&usqp=CAU"

#############
# SUBPROGRAMS
#############


def installPillow():
    # install pillow
    import asyncio
    asyncio.get_event_loop().run_until_complete(load_package("pillow"))


def get_ascii(pixel):
    # Get grayscale value of pixel
    grayscale = (pixel[0] + pixel[1] + pixel[2]) // 3
    # rescale from 0 to 9
    rescaled = floor(grayscale / 256 * len(ASCII))
    # Return ascii character
    return ASCII[rescaled]


def convert(image, width):

    # resize image in proportion
    print(f"original image was {image.width} by {image.height}")
    height = image.height // (image.width // width)

    # ==> TASK 2: Improve the scaling issue of square pixel to non-square characters by changing the number 1 in the line below to reduce the height
    height //= 1

    print(f"resized image is {width} by {height}")

    image = image.resize((width, height))

    ascii = []

    for y in range(image.height):
        row = ""
        for x in range(image.width):
            # Get the pixel at the position
            pixel = image.getpixel((x, y))
            # Add to the ascii string
            row += get_ascii(pixel)
        ascii.append(row)

    return ascii


def loadAndShow():
    image = load_image(IMG)

    # ==> TASK 1: Increase the size of the text image to 50 or 100 characters so it can be seen more easily
    ascii = convert(image, width=25)

    for row in ascii:
        print(row)

###############
# MAIN PROGRAM
###############


# ==> TASK 4: Extend the menu system so the user has a choice of images to display
while True:
    choice = input(
        "Choose \n1) Install pillow image library (must do first)\n2) Display image as text\n3) Quit\n> ")
    match choice:
        case "1":
            installPillow()
            print("installed....now run again...")
            break
        case "2":
            loadAndShow()
        case "3":
            break

# We can also encode the image directly in base64 - you can find sites which will convert an image to its base 64 form
# ==> TASK 3: Try moving this constant into the constants section and displaying it instead
IMG2 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUSFRISEhIREhIRERISEhISGBIRGRgYGBQZGRkYGBkcIS4lHB4rHxgYJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHxISHzQrISg0NDQ0MTQ0NDE0NDE3NjQ0NDQ0NDQ0NDQ0NTQ0MTQ0NDQ0NDQ0NDQ0NDQ0NDE0NDQ0NP/AABEIAMcA/gMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAAAQIDBAYFB//EAEMQAAIBAgMDCQQHBgQHAAAAAAECAAMRBBIhMUFRBQYTImFxgZGxMqHB0RQjQlJiovAzU4KSsuEHFnLCJENEVGNz0v/EABkBAQADAQEAAAAAAAAAAAAAAAABAgQDBf/EACMRAAICAgICAwEBAQAAAAAAAAABAhEDEiExBEETIlGBFGH/2gAMAwEAAhEDEQA/AOxLGMGI7Y7SCSSsZLMZASUAkGMkGkJIQB5pLNIxwCWYwDGRjEAlmMeYyMlADMY80UIIJZjDNIxwB5oZjxihAHmPGGYxQgDzGLMYGKAPMYixhCALNEWhCAIsYZjCKABYyJYxmIwCJYxoxv4RRpt8IBU22EDthBJIRiIRiAOSEjJCAOMQhAGIRRiASEcQjggICEIAxHFHACEJhxXK1Cno9RMw+yvXPkt5DaXZKTfRuinitzlp/Zp1WHGyp6m8mnOGkfbWpT7SAw9xv7pz+aF1Zf4Z1dHrxSvD4hKgvTdXHYfhtls6Jp9FGmuxQhCSQRMIGEAUDCKABkTGYjAFBNvhCCbfCAVHbCBhAGJISIkhBIxJSIkoA45GSgDEBFGIB53K/KooAKq56jC6rsAHFvlOcrcoYlzdqrL+Gn9WPdrNCv0lV6jH2m8hoAPKX8oYNFbqncNswZc0nbXRtx4oqk+zFS5RxC6iq5HBuv6zfR5w1R7VNH7roflMyUFOhP60kauGy7CJyjkmuUzq4RfDR6X+ZuNBr9jr8pVV5x1TpTpU17XZn9wtPLcWPyk1I1Gvuky8ma4shePDuh4rFVqg+sqtY/YTqL5Db4zKMOBawtNr0xpvEkqzhLJOXZ3jCMekZVpG0s6O4mhwBLeqoBJ0OkrG5MmTpHkGo1JgUJBB3ek6PkflwVLI5GfYL2F/HeZ5r4XM5A3C/mJRiOTASDbXiJtxuUTJNRl2dqYTnOTuVXo/V1s1SnubTMvdxE6ClVVwGRgynYRNkZKXRjlCURmKMxGXKAYozFAEYozEYAoJt8Io02+EApMIjtjgkYkhIiSEAYkhIxwCUd5ERwCUz4+pkp1G/CQO86D1mi88vl2rZUTez3Pco+ZEpkesWy0I3JI8zCU7G/ASyu+YwZQFHE6yt9NZ5E3XB6kVfJBlHu090pxD8Dul1QaXFtkoqU9e4+onO2dEipL318JdTiCbP1sklGp8DIZYrxqkJnHtAi/bJ4WpmUHslXKD5UI3nLbzvLsImUAdmsN8CiOKGg1Iud0sw1YL1TsNtJHFjQd49Z4+PxJR6YGgOt+4zpBclJPg6TDV/rLHf8J6SlGOy2vwnNpVs6a7cw+M9ehWBIvxt7jNUZGWUS/G4G40E8jBYp8O9geoxuVPvE6VG00N+yeHy3hxYsN2su/r9kVXP1kdLSqB1DqbhhcRzn+bGPzBqZP4l7xt/XZOgM1wkpRtGTJHWVAYozFLlBGIxmKAKNNvhEY02+EAzHbHIEyV4JJiAMiDJAwCV4xIR3gExHIgxiASvPB5VqZq1tyAL8T6+6e8JzeI1qVD/wCR/U/KZvKk1GkaPGjcmyFaoWsfKVljfvkyReV3u2m63rPMkm2ejFpFmb9eMidSfA/ODmxO7ZII4fMBtpt1h4XEOLQTJsNnZBBrC0oxtUqci6u66dl98qSU1D0jqo1Wne/fPQXTTfrKMNhxTTiTtl1AX14fq0EsjiRoNN4nhcvpbo2trqo7zPdxLm3jMtair5MwvlOYd4loumVkrRmJOenfcWH5bzfnsQe28wVzZ6Yt9th+QzWTp37J0umjm6PWoYmPF1A48+2eaHsAb90h0+tr7ROiyejm4+zPhX6KslQaDP1h+vETuzOAxI/qX1E7vDvdEPFFP5RNPiy7Rn8hcJlhigYprMoSMcRgCMabfCIxpt8IBkJgJEmAMElgkgZXeSBgEwY7yt3Cgk7ALmNHBAI2EXEixXssvBHBAYEEEAgjUEHYQYp41TEPRqOtNOkVr1Po9wrMDtegTodfaTjqNusN0ErPdE5lnuzH7zMfeZqTnPhmLJnanWs1qNRHR7gHSxFjs4zyqmIVNp3TH5UrpI2eKqtssd9pvoOOk8/Bcpq9aoguQKZ624lWGYA7yMwmPHVmqnISyp9xdGbvP2RPQo8lOE6cqKaUkCU6a7w7KGb3J3zjDG2m2d5ZVaSLa9bhqTsA1PhMGDSqldyUZM6hsj6FgTYW4bDOu5C5PCKKjgF22E62HZMeOAfGH8C0wT3Le3v98vLFrFN+ysctyaS6KHxKqhqDdplOhvsy995lwdMkmo+rNNGJwyu5Jv7V7DQG3HjJMQL8BMclTpGmPQVzpYRUtndM6YpXLKCOp1Se2wM0UxpI1F8BW2bOMhTsbfrfJVNRrFSSx290suirMdUAVKY/E5v/AAzY+wD9bDPM5RYqysPsVLn/AEkayTcopdACGLXtY8FM6O6spVM1hrqJQzWbw+MFfqr3CUOesO4iVj2S+iyvqe8/3ne01yqq/dVR5CcLgR0lVVGzMo8zO7Jm/wAWNWzH5L4SCIwvI3msyDMUCZEmAONPhIXjQ6+EAxk6xiRO2OCSV4wYhAQDLj3fRRbIw4akjW15DCYxU6rnKt+qzaAX3E7psqUw4ysLj47iO2edi8M1iLZlO8C48RMmTeMtlyjTi1lHV8HsA31GoOwjWUY7DU6iWqhSgIYMxy5SPtBtx7Z4IoMn7N3QcEZgPKCUi2tRne33yW9Y/wBK/Cf83/SGJovUNqVR6lNNj1SxseCkG5HlMH0FySXYC/3b6+O2e2HJGUDTYFUXl2H5MLkGpov3N57zu7px+05cHaoY1yYeRuSg5zkWpqdN2Y/KdNVph1KMOqylSOwxKAAAAABoANLd0YM2Qgoqvfsx5MjlK/RJNAANABYd05nDPnevV+/UbL3XsPcBPX5axfRUmI9t/q6Y/E3yFzPGVejRKY22u3lpM/ly6Ro8WPbJkcO2efyjigikX2AsxG0Abbdu4ds11qoRCxOwaDeTOeqgsDm2sbn4DuExRSXLNr/EeLyVj6rVjTRCz1nJRAbG/wB3Xs0vOnHKTU/q6tN6bLpZwV9Z53IGDAx+FbQAM7HwRp9Aq4pKjCnUpqaZ0D1LandYbh2ma1CE1d0zNKcoSqrRyn00HYwlbYztHnOgx3NXDsGYM1GwJJBGUDjYzkMfyI2b6iqzpb2nUpr2Db6TnkwOPbRbHmUukQxWP6wFxskEoq6s4AGwKyi2o26+7znn1eRMQWAa2W+pBN7dmk90UCUWmq5FUAbRe395TVRqmdH9jVSbqL/pHpMmJrAMACNBfXymvDYQiwLEhQBbumsZiLAXHdIikmQ+izmzSvUQ7dtQ/wAunwnYXnhck4ulT/aUzTcjKKqX8mXfs2jWevSrK4JVgwGmk9DBSVWYc9uV1wWExXgYp3M4ExXjMUALxpt8IjGm3wgFZp6wFOamTWMJBJlFOSFOacsYSAZhTjFKaQkkEigYnwattVT7pAcnJ90e+eiEkskq4RfolTkvZiTDBdgA7pPoprCSQSWSSIuzGKMYozZlngc5scwthqXt1B9Yw+yh+z3sPd3ys5KKtloRcnSPGxNUYms1S/1GHBCHcxuLsO87OwSp6m127SZbUVUVaKbFsWPFv7TFg8E+OqmjTJShTINeoNe5V/Efdt7/ADJbZJ0j0lrjhbPK5QxL1MtTKeiNTow+7MBmI7wJYF12bBOs574BKeCppTUIlGtTCKNwKsNu8m9yd5nLomgPEA+6Rlx6Oi2HJutizkqmDiFzbER2tx0tb3zqcMaKhnrPTFQG4FS3s2BBVd9zvHdOY5Domri1pqcpZHsdo0QkX7LgT3Kq5GyVVyuv2W9VO8ScbcftVorlSk9bpjxWIbFEBQy0A2gbQudxYcNNB4mFbDohsutgL8Ly8YoAWUAbNdOMzO1790rlntz2yccNeOkV1VzaAAd8yMAGKMBe11tvHHvm0bfGZqiZnLblQKO86n3WnJSbR1SoSJYec0YeoAQLSonQefnIoNkmMmJRTPfWrSqUyrABjsOm2eDhMSaNTb1b5WHEEy1H07jPPrjUnvnb5W6/UcfjVNemduUiyTXhqd0pk7SiE/yiTNOesjyn2YMsWWbzTkTS7IoGErGia+E2GlGlLXwigNk1gElrLrDLJIK8sYSWWjtAKwkYSTtGBBJEJGFkrRhYAssYWStGIBmx+IFKm9Qi+UdUcWOijztOPY5Azsc1WoSxJ7dpnv8AOh/q6a7jUBPgp+YnLYupbXadJ5/lTe2qN3jQWu36UdC9Z0oUv2lU2LH7Cj2nPYBPoXJXJaYamlKmLKupJ2sx1LMd5JnNcwaQf6TiCOtnFBDwVVDt5lh5TswZ38XGox29s4+Tkcpa+kc3z9T/AIN//ZS/rnD7FUfhnZ8/6v1FOnvetfwVT8Ss4nFnKunCZvK5yfxGnxVWP+m7mEnSY923U6Lk97dX4z6ZicElQZalNXXcGANu47vCcH/hTQLHF1zsZ0pKe67N/tn0W82YYJQoy55tztHzLHUQMRVXDpVenTOQIgqVesvtM20jW9geEzHlQLdStTMCQwykWIOoPCfVkQLooAFybAAak3J0nx3FMXerf2nquD3ljeY8+FQad9mnBlclX4ephK7MpOQgE9W9ri2lm+ctZbAAbd54nfLMNTsovtt8TK8RUVLFiBa+3SZEuTVYsmzujTS3fMg5SQgsAzKlgzqrFVPAtawPfLqOLSp7LKd9pZQoq5WaHpzFUTM1u0AeJtPQzXsJVSQdLT7alMfnWXSVkW6PoCUgABwUDyEOjl5itPZPIKDTkeimgiFpJBmNGSo0dfA/CXWkqI18D8IBnZNYZJaw1itIBDJDJLBHAK8sWWW+EMsElWWPLLckMkAryx5ZIgwzQDm+eB6tEcXc+Sj5zlsT8J0XOypmq0k3JTZvFmt/tE5+trPK8h3lZ6WBVjR7v+HTjoa9PeuIL27HVbHzUzrrT5vze5XTDPWqFWdXVUVUK2OU3zEk+A7zPWxHPewJSgNAbXcE7OAE3YZVBWY8qubow87cV0uJyKbrh1yG33ycz/AfwzleW61lYDhFQ5dphWdi+d2LMSrXJJuT5zyeU+UVqAqmZidwVj8JhkpSyN0boOMYJWfVv8M6OTAUm31HqVD4vYf0zrs0+cc3+X6mHw1CgtOmwp01F7ubk6nUG20mekOdtX91S86g+M9GLSSR581cmztg8+Y4vk8jGYlALIKzPfgGOa35p7S85MRVDJTp06eljU6zBO0A6EzCWWmCASbnNUqNqXYnViZk8qcZJJdmjxoSi22KvXCKSdAoM5jD44Ypma9wD1B2bjK+U+UPpb/RqdRVVT12O+21V+8eyX1sPTpPh+hp9GmTon6xYu4uQ7X+0btfuEzrDLRyNKyR21LMS/Q0sfSOlPFYYMvZWQqVt3rm8hOT5GxTB8mdgb9U3OhtfyndY/DCpTy8JwXI+HZsQQRqjvm7LHL6+kvCW8Gn6Eo6y49neclYrMbNow0Yds14liCrgapZh3g3HpPDxbdGyuDssG9J7VGqKiAi15wVou6PpOHqioiOuqsoYHvEstOW5pcoFWOFcEizPTO21tWU9mtx3zqrz1sU94JnlZIayaI2haO8LzqcyNpOkNfD5SN5Kn8IBW41haY2xRvuk0xXGRYNNoCVfSF4xfSViyS+Amc4peBkTi+Aiwa5W+IUb/LWYXrFtp8pXIsk1tjRuXzNpU2Kc7wO4D1lMYkWxRkx3JyVv2gLW2HM4I7iDpMuG5Do02zKrNcEEVGaoCDus156yld4Jlq11GxBKaK7Zbd1RzWI5mYaoSyUTTY76LPTH8vs+6ZKnMWqNadRGH3aqhT/ADofhOzONO4AStsUx3yaQ2Z82xHNmvRDdJhWZdoanlrDyXW3hOexl06opsNdlsvu2+6fZHcnaTKqlNW0ZQw4MA3rKPGr4LrI/Z82wFe9NAeqbWsdCPOXOw438Z3NTknDt7VCif4E+UpPN/C/9vS8AR6S1Mo2ji6XLHRKyuG6MdY6EWPEaa90yYnllat+vanqLC5Ld/ATvG5u4Y/9PT/N84f5ew37hPzfOcZYE5bHaOaSjqfNaWLoUzdVYH8IRfeLmaa+PLoGARaauh1z57g6Wn0A83MN+4p/m+cP8vYb9wngan/1Oji2qZRTp2ji63K5AsiML/bqCyDTfrczm+Tay0Kr1BVSszk5wQ6Em51BZdNs+rHm5hj/AMr81T5yac1qB2UPe4+M5xwKKa/TpLPJtM+edKMTUpglUpg56gqMi3y7F27zNeIrrh26Sm6ZCevTVg9u1bbuyd8OZeHb2qSj+KofjLl5lYTfTJ7mcfGW+Ba0VeeW1nL4DlOpTIq07IXQWuFcFTY68L6bJ0vJPOjpHSlVRQ9Q5VZDtPah18bmbU5q4QadDccC9QjyzTbguRsNQOalQpU2+8qjN/MdZ2hHVao4zlu7ZrjtJQnQoRyySbfCEabfCAeOy6xZZc66xWlCSvLDLLLR5YBVaGWW5YZIBVlhll4SMU4BnywyzSKUsFERRNmHLDozPRFISQpiKFnnCkeEmMM09ELHaTRFmAYM8ZJcD2zdCKFmQYEcTJfQV4maY4Bl+grxMX0FeJmqEkWZhg07fOTGFQfZHvl0IFla01GxQJO0cIIFCOEkWKEcIBEwkiIrQBSdLb4fKRtJJt8IBkakeHpF0J4ekISoF0J4ekYonh6QhAJCieHpGKJ4ekUIBIUjw9JIUjw9IQgEhTPD0kgh4ekIQSGQ8PSPIeHpFCAPKeHpDKeHpCEAMp4ekMp4ekIQB5Tw9IZTw9IQgBlPD0hlPD0hCAGU8PSGU8PSEIIDKeHpDKeHpCEkBlPD0hlPD0hCAGU8PSGU8PSEIAZTw9IZTw9IQgBlPD0jVTfwhCAf/9k="
