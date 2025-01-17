'''RPN Expression'''

expr = "7 __ 3 * _ 5 __ + 1 2 _ _ - 5 4 - _"

'''Evaluation'''

stack = []

for token in ____.split(" "):

  if ____ in "+-*/":

    op2 = _____.pop()
    op1 = stack.___()

    match token:
      case "___": stack.append(___ + op2)
      case "___": stack.append(op1 - ___)
      case "*": stack.append(op1 _ op2)
      case "/": stack.append(op1 _ op2)

  else:

    stack.append(int(_____))

print(stack._____)
