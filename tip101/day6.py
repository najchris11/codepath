# def is_long_pressed(name, typed):
#     namePtr, typedPtr = 0, 0
#     while typedPtr < len(typed):
#         if typed[typedPtr] == name[namePtr]:
#             namePtr += 1
#             typedPtr += 1
#         elif typed[typedPtr] == typed[typedPtr-1]:
#             typedPtr += 1
#         else:
#             return False
#     return True

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

# def find_content_children (size, greed):
#     numOfHappyKids = 0
#     greedPtr, sizePtr = 0,0
#     while sizePtr < len(size) and greedPtr< len(greed) :
#         if size[sizePtr] >= greed[greedPtr]:
#             numOfHappyKids += 1
#             greedPtr += 1
#         sizePtr += 1
#     return numOfHappyKids

# g = [1,2,3]
# s = [1,1,3]
# # There are 3 children and 3 cookies
# # child `0` has a greed factor of 1
# # cookie `0` has a size of 1 --> content child

# # child `1` has a greed factor of 2
# # cookie `1` has a size of 1, this child will not be content

# # child `2` has a greed factor of 3
# # cookie `2` has a size of 3 --> content child

# print(find_content_children(s, g) )
# # Output: 2 

# g = [1,1]
# s = [2,2,2]
# # There are 2 children and 3 cookies
# # child `0` has a greed factor of 1
# # cookie `0` has a size of 2 --> content child

# # child `1` has a greed factor of 1
# # cookie `1` has a size of 1 --> content child

# print(find_content_children(s, g) )
# # Output: 2 

def valid_palindrome(s):
    frontPtr, backPtr = 0, len(s)-1
    

def is_palindrome(s):
    frontPtr, backPtr = 0, len(s)-1
    while frontPtr < backPtr:
        if s[frontPtr] != s[backPtr]:
            return False
        frontPtr += 1
        backPtr -= 1
    return True

s = "aba"
s2 = "abca"
s3 = "abc"

print(is_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))