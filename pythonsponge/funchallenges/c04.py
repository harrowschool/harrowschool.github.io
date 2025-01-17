river = [" " for _ in range(40)]
ships  = {"lifebuoy": "o", "raft": "---", "canoe": "\___/", "viking ship": "\(o)(0)(o)/"}
pieces = 0

def printRiver(river):

  result = "|"
  
  for position in range(len(river)):
    if position in misses:
      result += "~"
    elif position in hits:
      result += river[position]
    else:
      # ==> TASK: CHANGE THIS TO A SPACE CHARACTER TO INDICATE RIVER POSITIONS NOT YET SHOT AT
      result += ""
      
  result += "|"
  
  print("RIVER:\n", result)

def placeBoat(river, boat, position):
  length = len(ships[boat])
  for count in range(position, position + length):
    river[count] = ships[boat][count-position]
  return length
  
def fire(pos, river, hits, misses):
  # ==> TASK: FIX THE ERROR HERE: THE CODE CURRENTLY CHECKS TO SEE IF A CELL IS EMPTY AND THEN SCORES A HIT!
  # ==> ...BUT IT SHOULD CHECK IF IT IS NOT EMPTY AND THEN SCORE A HIT!
  if river[pos] == " ":
    print("Direct Hit!")
    hits.append(pos)
  else:
    print("Miss!")
    misses.append(pos)

# place the boats at certain locations on the river for the start of the game
pieces += placeBoat(river, "lifebuoy", 0)
pieces += placeBoat(river, "canoe", 34)
pieces += placeBoat(river, "viking ship", 9)
pieces += placeBoat(river, "raft", 26)

gameOver = False
hits = []
misses = []

while not gameOver:

  printRiver(river)
  
  shot = int(input("Enter Position To Fire At [1-40] or -1 to quit: "))
  
  if shot == -1:
    break
  
  fire(shot-1, river, hits, misses)
  print("Hits:", hits, "Misses:", misses)
  
  if len(hits) >= pieces:
    # ==> TASK: SOMETHING NEEDS FIXING HERE! THE GAME DOESN'T SEEM TO CURRENTLY END!
    gameOver = False

if gameOver:
    printRiver(river)
    print("All ships sunk - well done!")