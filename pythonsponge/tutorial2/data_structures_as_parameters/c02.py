def get_longer_list(lst):
  for count in range(3):
      lst.append(count)
  return lst

nums = [10, 9, 8]
new_nums = get_longer_list(nums)

print(f"original list: {nums}")
print(f"final list: {new_nums}")