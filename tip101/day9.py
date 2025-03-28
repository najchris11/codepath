# def repeat_hello(n):
# 	if n > 0:
# 		print("Hello")
# 		repeat_hello(n - 1)
		
# repeat_hello(5)

# def repeat_hello(n):
#     for i in range(n):
#         print("Hello")
# repeat_hello(5)

# def factorial(n):
# 	if n == 0 or n == 1:
# 		return 1
# 	return n * factorial(n-1)

# print(factorial(5))


# def sum_list(lst):
# 	if len(lst) == 0:
# 		return 0
# 	return lst[0] + sum_list(lst[1:])
# lst = [1, 2, 3, 4, 5]
# print(sum_list(lst))

# def is_power_of_two(n):
# 	if n == 2:
# 		return True
# 	if n < 2:
# 		return False
# 	return is_power_of_two(n/2)

# print(is_power_of_two(256))

# def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

# def binary_search(lst, target):
# 	left = 0
# 	right = len(lst) - 1
# 	while left <= right:
# 		mid = left+(right-left)//2
# 		if lst[mid] == target:
# 			return mid
# 		elif lst[mid] > target:
# 			right = mid - 1
# 		else:
# 			left = mid + 1
# 	return -1

# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 11
# print(binary_search(lst, target))

# def find_last(lst, target):
# 	left = 0
# 	right = len(lst) - 1
# 	lastFound = -1
# 	while left <= right:
# 		mid = left+(right-left)//2
# 		if lst[mid] == target:
# 			lastFound = mid
# 			left = mid + 1
# 		elif lst[mid] > target:
# 			right = mid - 1
# 		else:
# 			left = mid + 1
# 	return lastFound

# lst = [1, 3, 5, 9, 9, 9, 13, 15]
# target = 9
# print(find_last(lst, target))


def find_floor(lst, x):
	if lst[0] > x:
		return -1
	return find_floor_helper(lst, x, 0)

def find_floor_helper(lst, x, lastIndex):
	if lastIndex >= len(lst)-1:
		return -1
	if lst[lastIndex+1] <= x:
		return find_floor_helper(lst, x, lastIndex + 1)
	else:
		return lastIndex
	
lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))