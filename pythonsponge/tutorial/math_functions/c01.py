import math

LAYOUT = "For number {): ceiling is {}, floor is {}, 1dp round is {}"

nums = [2.81, 3.15, 7.14, -4.65, 1.08, -7.54, 6.83, 4.65, 0.75, -3.56, 9.26, -8.07]
total = 0.0

for count in range(len(nums)):
  num = nums[count]
  ceiling_num = math.ceil(num)
  floor_num = math.floor(num)
  round_num = round(num, 1)
  print(LAYOUT.format(num, ceiling_num, floor_num, round_num))
  
