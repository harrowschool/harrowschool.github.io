nums1 = [2, 4, 6, 8, 10]
nums2 = nums1

print("adding 12 to nums1...")
nums1.append(12)

print("both variables share the same underlying object so both have changed:")
print("nums1 = ", nums1, "nums2 = ", nums2)

nums3 = list(nums1)

print("adding 14 to nums1...")
nums1.append(14)

print("nums1 and num3 have different underlying objects so only nums1 has changed:")
print("nums1 = ", nums1, "nums3 = ", nums3)