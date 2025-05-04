# def is_valid(s):
# 	lst = []
# 	dic = {"(": ")", "[": "]", "{":"}"}
# 	for c in s:
# 		if len(lst) == 0:
# 			lst.append(c)
# 		elif c == dic[lst[-1]]:
# 			lst.pop()
# 		elif c in dic.keys():
# 			lst.append(c)
# 		else:
# 			return False
# 	return True

# s = "(]"
# s2 = "(())"
# s3 = "()[]{}"

# print(is_valid(s3))

# def max_profit(prices):
# 	minPrice = prices[0]
# 	maxProfit = 0
# 	for day in prices:
# 		minPrice = min(minPrice, day)
# 		maxProfit = max(day-minPrice, maxProfit)
# 	return maxProfit

# prices = [7,1,5,3,6,4]
# prices2 = [7,6,4,3,1]
# print(max_profit(prices2))

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next


def shuffle_merge(head_a, head_b):
	lst = Node(0)
    ptr = lst
	aPtr = head_a
	bPtr = head_b
	ctr = 0
	while aPtr and bPtr:
		if ctr%2 == 0:
			ptr.value = aPtr.value
		else:
			ptr.value = bPtr.value
		ctr = ctr + 1
		ptr = ptr.next
	if