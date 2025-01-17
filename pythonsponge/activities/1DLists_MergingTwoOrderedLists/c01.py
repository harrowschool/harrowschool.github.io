# GLOBAL VARIABLES

nums1 = [5, 26, 68, 98, 103, 114, 134, 145, 187, 263, 277, 317, 342, 367, 380, 392, 447, 456, 498, 509, 545, 568, 577, 593, 632, 665, 670, 685, 702, 705, 705, 707, 716, 764, 797, 798, 804, 814, 854, 863, 872, 879, 880, 880, 940, 947, 965, 969, 970, 983]
nums2 = [18, 45, 59, 69, 75, 99, 128, 141, 165, 174, 187, 210, 224, 259, 259, 282, 318, 325, 332, 388, 410, 414, 428, 467, 474, 513, 517, 523, 566, 578, 614, 615, 635, 694, 698, 701, 701, 707, 713, 783, 797, 799, 846, 879, 894, 896, 924, 949, 952, 955]

# use this list to hold the merged items, maintaining an ascending order
mergedList = []

# MAIN PROGRAM

# ==> complete the processing loop
while len(nums1) > 0 and len(nums2) > 0:
  if nums1[0] < nums2[0]:
    mergedList.append(nums1[0])
    del nums1[0]
  else:
    ___________________________
    _____________

# add any remaining items from nums1 onto the merged list
for num in nums1:
  mergedList.append(____)

# ==> add any remaining items from nums2 onto the merged list


# output the result
print(mergedList)
