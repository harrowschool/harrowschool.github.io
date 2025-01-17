'''RPN Expression'''

# RPN Expression which represents the infix expression (3 + 4) * (1 + 2)
expr = "3 4 + 1 2 + *"

# TRACING ONLY
trace_mode = input(
    "Do you want to trace the algorithm? (y/n): ").lower() == "y"
if trace_mode:
  print("Press enter to go to the next step")
  print(f"\n{'TOKEN':<6} | {'STACK'}")
  print("-"*20)

'''Evaluation'''

stack = []  # initialise empty stack

for token in expr.split(" "):  # Loop through all tokens from left to right

  if token in "+-*/":  # operator

    op2 = stack.pop()  # pop second operand
    op1 = stack.pop()  # pop first operand

    match token:  # apply operator and push to stack
      case "+": stack.append(op1 + op2)
      case "-": stack.append(op1 - op2)
      case "*": stack.append(op1 * op2)
      case "/": stack.append(op1 / op2)

  else:  # operand

    stack.append(int(token))  # push to stack

  # TRACING ONLY
  if trace_mode:
    input(f"{token:<6} | {stack}")

# print result which is left as the only element on the stack
print(stack.pop())
