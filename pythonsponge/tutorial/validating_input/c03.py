valid = False
while not valid:
  choice = input("enter a whole number 0-99: ")
  if len(choice) <= 2 and choice.isdigit():
    # we now know we can convert it to an integer without an error
    num = int(choice)
    valid = True
		
print("nice, I also like", num)