initialArt = r'''                        ,,\\
                          \\\\\\,,__
                            \\``  ,,\\
                  ____,,..--""  ==____))
              ..""                ))
        ,,__//      ,,        \\//\\__
        \\__||        ))__--\\  \\__--``
              ``----------``  ``----``'''

print(initialArt)

print("initialArt length:", len(initialArt))

prevCh = initialArt[0]
prevCount = 0
compressedArt = ""

for ch in initialArt:
  if ch == prevCh:
    prevCount += 1
  else:
    compressedArt += f"{prevCh}*{prevCount}#"
    prevCh = ch
    prevCount = 1

# we need to ensure we don't miss of the final run of characters
compressedArt = compressedArt + f"{prevCh}*{prevCount}"

print("compressedArt length:", len(compressedArt))
print(compressedArt)

# ==> TASK 1 : CAN YOU CALCULATE AND OUTPUT THE % SAVING?



# ==> TASK 2: NOW CAN YOU RECREATE THE ORIGINAL OUTPUT FROM compressedArt?




