import random
import time

def printWitch(lives):

    image = f"""
                                                   
   .'   `'-._                                    
  / ,        `'-_.-.                          
 / /`'.       ,' _  |                          
`-'    `-.  ,' ,'\\/                                  
          \, ,'  ee`-.        
          / ./  ,(_   \       ,    
         (_/\\\ \__|`--'      ||
         ///\\|     \         ||                  You have {lives} lives left...
         ////||-./`-.|    .--||      
            /     `-.__.-`_.-.|          
            |      '._,-'`|___|    `;
            /   '.        |/ || ,;'`
            |     '.__,.-`   || ':,    
            |       |        || ,;'      
            /       /     _,.||oOoO.,_
           |        |     \-.O,o_O..-/
          /         /     /          \  
    """
    print(image)

def printWitchAndBat():
         
    image = """
                                                     \--/
   .'   `'-._                                     /`-'  '-`\\
  / ,        `'-_.-.                             /          \\
 / /`'.       ,' _  |                           /.'|/\  /\|'.\\
`-'    `-.  ,' ,'\\/                                   \/
          \, ,'  ee`-.        
          / ./  ,(_   \       ,    
         (_/\\\ \__|`--'      ||
         ///\\|     \         ||
         ////||-./`-.}    .--||      
            /     `-.__.-`_.-.|          
            |      '._,-'`|___}    `;
            /   '.        |/ || ,;'`
            |     '.__,.-`   || ':,    
            |       |        || ,;'      
            /       /     _,.||oOoO.,_
           |        |     \-.O,o_O..-/
          /         /     /          \  
    """
    print(image)

def printCatOnPumpkin():

    image = """                             .                                  
                          ,''`.         _                        
                     ,.,'''  '`--- ._,,'|                        
                   ,'                   /                        
              __.-'                    |                        
           ''                ___   ___ |                        
         ,'                  \(|\ /|)/ |                        
        ,'                 _     _     `._                      
       /     ,.......-\    `.      __     `-.                    
      /     ,' :  .:''`|    `:`.../:.`` ._   `._                
  ,..,'  _/' .: :'     |     |      '.    \.    \                
 /      ,'  :'.:  / \  |     | / \   ':.  . \    \              
|      /  .: :' ,'  _)  ".._,;'  _)    :. :. \    |              
 |     | :'.:  /   |   .,   /   |       :  :  |   |              
 |     |:' :  /____|  /  \ /____|       :  :  |  ,'              
  |   /    '         /    \            :'   : |,/                
   \ |  '_          /______\              , : |                  
  _/ |  \'`--`.    _            ,_   ,-'''  :.|         __      
 /   |   \..   ` ./ `.   _,_  ,'  ``'  /'   :'|      _,''/      
/   /'. :   \.   _    [_]   `[_]  .__,,|   _....,--=/'  /:      
|   \_| :    `.-' `.    _.._     /     . ,'  :. ':/'  /'  `.    
`.   '`'`.         `. ,.'   ` .,'     :'/ ':..':.    |  .:' `.  
  \.      \          '               :' |    ''''      ''     `.
    `''.   `|        ':     .      .:' ,|         .  ..':.      |
      /'   / '"-..._  :   .:'    _;:.,'  \.     .:'   :. ''.    |
     (._,.'        '`''''''''''''          \.._.:      ':  ':   /
                                             '`- ._    ,:__,,-'
                                           ``''"""
    print(image)

def getWitchWord():
    with open("c11_words.txt") as file:
        words = file.read().splitlines()[0].split(",")
    return random.choice(words).lower().strip()

def updateSolvedAndLives(guess, answer, solved, lives, trickState):
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                solved[i] = guess
    else:
        lives -= 1
        if trickState:
            print("Uh oh... you guessed wrong! You lose two lives! >:)")
            lives -= 1
    return solved, lives

def doTreat(answer, solved):
    while True:
        index = random.randint(0, len(answer) - 1)
        if solved[index] == "_":
            letter = answer[index]
            for pos in range(len(answer)):
                if answer[pos] == letter:
                    solved[pos] = letter
            break
    return solved

def trickOrTreat():
    print("Trick or treat!! Would you like to take a risk?\nIf you get a treat, all instances of one letter in the word shall be revealed.\nIf you get a trick, then if your next guess is wrong you will lose two lives! If you manage to guess right, however, play continues as normal. What will it be? Will you take the risk?")
    while True:
        # Challenge 5 ==> Can you allow the user to enter 'N' and 'Y as well as 'n' and 'y'?
        risk = input("Enter 'y' or 'n' to choose:> ")
        if risk == 'n':
            print("Very well, playing it safe! Your next guess will be treated as normal 🎃")
            return "normal"
        elif risk == 'y':
            print()
            print("Taking a risk, are we? Let's see what you get...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            if random.randint(1, 2) == 1:
                print("Trick!!! Mwahahahaha - you will lose two lives if you guess wrong! 😈")
                return "trick"
            print("Treat!!! Here's some candy - or chocolate if you prefer: 🍬🍫. In addition, all instances of one letter in the word shall be revealed! Which gift did you like better?")
            return "treat" 
        print("Looks like you typed it incorrectly... here's a ghost for your troubles: 👻")

answer = getWitchWord()
solved = ["_"] * len(answer)
guessedLetters = []
lives = 6

message = "On halloween night, you and your friends decide to go trick or treating. You knock on the door of a spooky house, and a witch answers. She says that you have 6 lives to guess the word she is thinking... If you fail, she will force you to drink a potion that will turn you into a bat! If you win, you can leave unscathed. Watch out for tricks and treats along the way..."

print()
print(message)
print()

while True:

    trickState = False
    printWitch(lives)
    # Challenge 2 ==> Can you fix the next line so that you lose if you have fewer than 0 lives as well?
    if lives == 0:
        print("You lose! The word was " + answer + ".")
        print("You have become a bat!! You'd better get used to being awake at night time...")
        printWitchAndBat()
        break
    print("Guessed letters: " + ", ".join(guessedLetters))
    print("word: " + " ".join(solved), end="")

    # Challenge 1 ==> Can you change the line below (just one number!) so that there is a 1 in 5 chance of getting a trick or treat?
    if random.randint(1, 6) == 1:
        print()
        result = trickOrTreat()
        if result == "trick":
            trickState = True
        elif result == "treat":
            solved = doTreat(answer, solved)
            print()
            print("Here is your treat :)")
            print("word: " + " ".join(solved))

    # Challenge 4 ==> Check if solved is the same as answer and, if so, print a suitable win message and break

    print()
    while True:
        # Challenge 3 ==> Can you add verification to ensure that the player only enters a single letter?
        guess = input("Guess a letter: ")
        if guess in guessedLetters:
            print("You have already guessed that letter!")
            continue
        break
    guessedLetters.append(guess)

    solved, lives = updateSolvedAndLives(guess, answer, solved, lives, trickState)
    if solved == list(answer):
        print()
        print("You win! The word was " + answer + ".")
        print("After running away from that house as far as possible, you return home to your cat with a pumpkin full of sweets and chocolate.")
        printCatOnPumpkin()
        break
   