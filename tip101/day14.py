# def contains_duplicate(nums):
# 	numSet = set(nums)
# 	return not len(numSet) == len(nums)

# nums = [1,2,3,4]
# print(contains_duplicate(nums))

# def remove_element(nums, val):
# 	ret = 0
# 	for num in nums:
# 		if not num == val:
# 			ret += 1
# 	return ret
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(remove_element(nums, val))

# def gcd_of_stings(str1, str2):
# 	largestSub = ""
# 	biggerStr = str1 if len(str1)>len(str2) else str2
# 	smallerStr = str2 if len(str1)<len(str2) else str1
# 	# rPtr = len(smallerStr) + 1 
# 	# while largestSub == "":
# 	rPtr = len(smallerStr)
# 	for i in range(len(biggerStr) - len(smallerStr) + 1):
# 		print(biggerStr[i:i+rPtr])
# 		if biggerStr[i:i+rPtr] == smallerStr:
# 			largestSub = biggerStr[i:i+rPtr]
# 	return largestSub
# str1 = "ABCABC"
# str2 = "ABC"
# print(gcd_of_stings(str1, str2))

from math import gcd

def gcd_of_strings(str1, str2):
	if str1 + str2 != str2 + str1:
		return ""
	return str1[:gcd(len(str1), len(str2))]

str1 = "ABABAB"
str2 = "ABC"
print(gcd_of_strings(str1, str2))