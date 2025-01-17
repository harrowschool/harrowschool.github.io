class Stack:
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return self._items == []
    
    def peek(self):
        return self._items[-1]

    # ==> add the two essential stack methods from the last example below


def displayCurrentText():
    print(f"Document text:\n{' '.join(words)}")

actions_stack = Stack()
words = []

while True:
    action = input("Choose 1) add word, 2) toggle last word lower/upper case, 3) undo, 4) quit: ")
    if action == "1": # user adds new word
        word = input("Enter a lowercase word to add: ").lower()
        words.append(word)
        actions_stack.push(action)
        displayCurrentText()
    elif action == "2": # user toggles case of last word
        if len(words) == 0:
            print("No word to change")
            continue
        words[-1] = words[-1].swapcase()
        actions_stack.push(action)
        displayCurrentText()
    elif action == "3": # user wants to undo!
        if actions_stack.is_empty():
            print("Nothing to undo")
        else:
            # ==> complete the code below to undo the last action
            action = actions_stack.___()
            if action == "1":
                words = ______
            elif action == "2":
                words[-1] = ______
            displayCurrentText()
    elif action == "4": # user quits
        break
    else:
        print("choose 1-4 only")

displayCurrentText()
print("Goodbye!")