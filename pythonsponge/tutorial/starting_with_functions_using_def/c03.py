def check_user():

  print("enter two whole numbers which add to 10 to check that you are human!")
  num1 = int(input())
  num2 = int(input())

  if num1 + num2 == 10:
    return True

  return False

result = check_user()

if result:
  print("you are human!")
else:
  print("maybe you are a bot!")