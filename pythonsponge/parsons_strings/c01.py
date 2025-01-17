firstname = input("enter firstname: ")
surname = input("enter surname: ")
joined = (firstname + surname).lower()
username = joined[0:3] + joined[-3:]
username += str(len(surname))
print("your username is:", username)