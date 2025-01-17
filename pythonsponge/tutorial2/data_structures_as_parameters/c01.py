def change_list(lst):
  lst.sort()
  print("the list contents range from", lst[0], "to", lst[-1])

nums = [4, 2, 7, 9]
change_list(nums)

print("note the original list outside the function has now changed...")
print(nums)
print("...this may or may not be what you wanted!")