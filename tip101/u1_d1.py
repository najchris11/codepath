# def hello_world():
#     print("Hello, World!")

# hello_world()

# def todays_mood():
#     mood = "😅"
#     print("Today's mood: " + mood)

# todays_mood()

# def print_menu(menu):
#     print("Lunch today is: " + menu);

# print_menu("🍕");

# def sum(a, b):
#     return a + b

# num1, num2  = 20, 8
# doubledSum = sum(num1, num2) * 2
# print(doubledSum)

# def product(a, b):
#     return a * b

# print(product(22, 7))

# def classify_age(age):
#     if age < 18:
#         return "child"
#     else:
#         return "adult"
    
# output = classify_age(18)
# print(output)
# output = classify_age(7)
# print(output)
# output = classify_age(50)
# print(output)

# def what_time_is_it(hour):
#     if hour == 2:
#         return "taco time 🌮"
#     elif hour == 12:
#         return "peanut butter jelly time 🥪"
#     else: return "nap time 😴"

# time = what_time_is_it(2)
# print(time)
# time = what_time_is_it(7)
# print(time)
# time = what_time_is_it(12)
# print(time)

# def blackjack(score):
#     if score == 21: print("Blackjack!")
#     elif score > 21: print("Bust!")
#     elif score >= 17 and score < 21: print("Nice Hand!")
#     else: print("Hit me!")

# blackjack(24)
# blackjack(19)
# blackjack(21)
# blackjack(10) 


# def get_first(list):
#     if len(list) == 0: return None
#     else: return list[0]

# print(get_first([3, 1, 6, 7, 5]))



# def get_last(list):

#     if len(list) == 0:
#         return None
    
#     else:

#         return list[-1]
    

# print(get_last([3, 1, 6, 7, 5]))


# def counter(stop):

#     for x in range(1, stop + 1):
#         print(x)


# counter(7)

def sum_ten():
    rVal = 0
    for num in range(10 + 1):
        rVal += num
    print(rVal)

sum_ten()