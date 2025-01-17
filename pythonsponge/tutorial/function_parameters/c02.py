def say_hello(greeting_type, name):
  layout = "unknown greeting type"
  if greeting_type.lower() == "formal":
    layout = "Dear {0}"
  elif greeting_type.lower() == "informal":
    layout = "Hiya {0}"        
    
  return layout.format(name)

firstname = input("enter your firstname: ")
choice = input("enter your greeting type - formal or informal: ")

message = say_hello(____, _________)
print(_______)