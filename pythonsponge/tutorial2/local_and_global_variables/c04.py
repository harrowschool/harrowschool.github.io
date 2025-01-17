import time

def coundownMessageChange():
    for num in range(3, 0, -1):
        print(num)
        time.sleep(1)
    message = "game over"

message = "game afoot!"
print("The message is currently: ", message)
coundownMessageChange()

# Note: the message hasn't changed because the message variable inside the function was a shadow variable
print("The message is now: ", message)
