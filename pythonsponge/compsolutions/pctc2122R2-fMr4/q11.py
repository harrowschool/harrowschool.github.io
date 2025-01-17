digits = input()
freq = [0] * 10

def get_median(fr_list):
    med_index = (sum(fr_list) + 1) // 2
    count = 0
    index = 0
    while count < med_index:
        count += fr_list[index]
        index += 1
    return index - 1

result = ""

for i in range(0, len(digits)):
    freq[int(digits[i])] += 1
    result += str(get_median(freq))

print(result)

# as an alternative which uses two heaps to efficiently maintain the median:

# import heapq

# left = []
# right = []
# result = ""

# digits = input()

# for digit in digits:
  
#   heapq.heappush(left, -int(digit))

#   if left and right and -left[0] > right[0]:
#     heapq.heappush(right, -heapq.heappop(left)) 

#   if len(right) > len(left):
#     heapq.heappush(left, -heapq.heappop(right))
#   elif len(left) > len(right) + 1:
#     heapq.heappush(right, -heapq.heappop(left))
  
#   result += str(-left[0])

# print(result)