# def is_subsequence(lst, sequence):
#     # taking in two lists and returning bool
#     # true if the numbers come in the same order
#     # so we can keep a pointer to a position in the lst, and then iterate through sequence and if index of is < pos we can continue
#     currPos = 0
#     for num in sequence:
#         # this only works if all the numbers in subsequence exist in lst
#         if lst.index(num, currPos, len(lst)) < currPos:
#             print(currPos)
#             return False
#         else: 
#             currPos = lst.index(num, currPos, len(lst))
#             print(currPos)
#     return True

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

# def is_subsequence(lst, sequence):
#     i =0   
#     for nums in lst:
# #check if nums in in sequence
#         if sequence[i] == nums:
#             i+= 1
#     if(i == len(sequence)):
#         return True
#     else: return False

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))


# def create_dictionary(keys, values):
#     retVal = {}
#     for i in range(len(keys)):
#         retVal[keys[i]] = values[i]
#     return retVal

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))

# def print_pair(dictionary, target):
#     if target in dictionary: print("Key: " + target + "\nValue: " + dictionary[target])
#     else: print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")

# keyTotal, valueTotal = 0, 0
# def keys_v_values(dictionary):
#     keyTotal = sum(dictionary.keys())
#     valueTotal = sum(dictionary.values())
#     if keyTotal > valueTotal: return "keys"
#     elif valueTotal > keyTotal: return"values"
#     else: return "balanced"
# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)


def restock_inventory(current_inventory, restock_list):
    for k,v in restock_list.items():
        if k in current_inventory:
            # chose not to do this so that we could look ahead

    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}