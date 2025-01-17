# ordered data is required for binary search
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

target = int(input("Enter a positive whole number to search for between 1 and 40: "))

low = 0
high = len(nums) - 1
found = False

while low <= high:

  # Note integer division to retain a whole index number
  mid = (low + high) // 2
  
  if nums[mid] == target:
    found = True
    break
  elif nums[mid] < target:
    low = mid + 1
  else:
    high = mid - 1

print("Found!" if found else "Not found...try again!")
