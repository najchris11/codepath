# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# head = Node(4, Node(3, Node(2)))
# print(head)


# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def count_element(head, val):
# 	count = 0
# 	curr = head
# 	while curr:
# 		if curr.value == val: count += 1
# 		curr = curr.next
# 	return count

# head = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(head, 1))

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
        
# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()


# # I have a bug! 
# def remove_tail(head):
#     if head is None: # If the list is empty, return None
#         return None
#     if head.next is None: # If there's only one node, removing it leaves the list empty
#         return None 
		
# 	# Start from the head and find the second-to-last node
#     current = head
#     while current.next.next: 
#         current = current.next

#     current.next = None # Remove the last node by setting second-to-last node to None
#     return head

# head = Node(3, Node(1, Node(2, Node(1))))
# remove_tail(head)
# print_list(head)


# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def find_middle_element(head):
#     slow = fast = head
#     if not fast.next:
#         return head.value
#     if not head:
#         return None
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#     # if not fast.next:
#     #     return slow.next.value
#     return slow.value

# # head = Node(1, Node(2, Node(3)))
# head = Node(3, Node(1, Node(2, Node(1))))
# print(find_middle_element(head))

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def is_palindrome(head):
# 	pass

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
	pass

# temp 
# head 1 -> 2
# curr 1