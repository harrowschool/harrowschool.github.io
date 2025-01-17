# Nested Goto Loop

_By Abhinav Gupta_

## Task Two: Summing Dice

**Print a table of sums for two dice rolls.** Normally you could use the following loop:

```Python3
for i in range(1,7):
	for j in range(1,7):
		print(f"Dice Rolled {i}, {j} Sum to: {i+j}")
```

## Hints

- Use the same goto loop as before but twice! Where do we want the goto to loop to? `goto(6)`
