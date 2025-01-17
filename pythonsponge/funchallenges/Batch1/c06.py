STEM = "  ‖  "
SPACING = "     "

FLOWER = [" ### ", "##0##", " ### "]
FLOWER_HEIGHT = 3
STEM_HEIGHTS = [3, 4, 5]
NUM_PLANTS = len(STEM_HEIGHTS)

num_days_passed = 0
heights = [0] * NUM_PLANTS
lines = ["-" * (len(SPACING) + len(STEM) + 2) * NUM_PLANTS]

while True:
  print("Day", num_days_passed + 1)
  line = SPACING

  for plant in range(NUM_PLANTS):

    # checks if the STEM should continue growing
    if heights[plant] < STEM_HEIGHTS[plant]:
      # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
      line += ____ + SPACING
      # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
      heights[_____] += 1

    # checks if the FLOWER HEAD should grow
    elif heights[plant] < STEM_HEIGHTS[plant] + FLOWER_HEIGHT:
      line += FLOWER[plant] + SPACING
      # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
      heights[_____] += 1

    # runs if plant is done growing
    else:
      line += SPACING + " " * len(STEM)
  
  # ==> TASK: WHAT SHOULD COMPLETE THIS GAP ON THE NEXT LINE?
  lines.insert(0, ____)
  # Note: we insert at the start of the list because the latest line will be highest and should be printed first
  
  print("\n")

  for line in lines:
    print(line)

  num_days_passed += 1

  # makes you press enter at the end of every day
  check = input("Press enter to progress to next day or q to quit: ")

  if check == "q":
    break