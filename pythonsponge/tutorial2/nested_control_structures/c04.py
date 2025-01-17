n = int(input())

current_term = "1"

for _ in range(n-1):
    next_term = ""
    current_letter = current_term[0]
    counter = 1
    
    ___ ch __ current_term[1:]:
        if ch == current_letter:
            counter += __
        else:
            next_term += str(counter) + current_letter
            current_letter = ch
            counter = __
    
    next_term += str(counter) + current_letter
    current_term = _________
    
print(current_term)
