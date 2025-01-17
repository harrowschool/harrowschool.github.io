letter_num = ord(input("enter initial uppercase letter: ")) - ord("A")
to_add = int(input("number of letters to add on? "))
letter_num += to_add
letter_num = letter_num % 26 
print(chr(letter_num + ord("A")))