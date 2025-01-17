from random import choice

names = ["Jack", "Freya", "Dominic", "Prada", "Mark", "Sarvish"]
options = ["naughty", "nice"]
presents = {
  "naughty": ["a piece of coal", "one sock", "a mouldy sweet", "stinky cheese"],
  "nice": ["games console", "teleporting machine", "automatic homework finisher"]
}  

print("SANTA'S CHRISTMAS PRESENT LIST GENERATOR:")

# ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
for name in _____:
  print("checking up on", name)
  sleep(1)
  print("....were they naughty or nice this year?")
  sleep(1)
  print("...calculating total nice actions - total naughty actions, please be patient...")
  sleep(2)
  result = choice(options)
  # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
  print("RESULT:", ______)
  sleep(1)
  print("...detecting allocated present...please wait...")
  sleep(2)
  present = choice(presents[result])
  # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
  print("PRESENT ALLOCATED:", _______, end="\n\n") 