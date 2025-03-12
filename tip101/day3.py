# def count_mississippi(limit):
#     for num in range(1, limit):
#         print( f"{num} mississippi")

# count_mississippi(6)

# def swap_ends(my_str):
#     return my_str[-1] + my_str[1:-1] + my_str[0]

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# def is_pangram(my_str):
#     alphabetDict = {}
#     strList = my_str.split(" ")
#     for word in strList:
#         for char in word.lower():
#             if char not in alphabetDict: alphabetDict[char] = 1
#     return len(alphabetDict) >= 26

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

# def reverse_string(my_str):
#     # retStr = ""
#     # for i in range(len(my_str)-1, -1, -1):
#     #     retStr += my_str[i]
#     return my_str[::-1]
# my_str = "live"
# print(reverse_string(my_str))

# def first_unique_char(my_str):
#     for i in range(len(my_str)):
#         if my_str.count(my_str[i]) == 1: return i
#     return -1
    

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# def min_distance(words, word1, word2):
#     minDist, minWord1, minWord2 = -1, words.find(word1), words.find(word2)
#     while words.find(word1, minWord1, len(words))
#     #unfinished

date = "11-06-2001"
print(date[3:5])