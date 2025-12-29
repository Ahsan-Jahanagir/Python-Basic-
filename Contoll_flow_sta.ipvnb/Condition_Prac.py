# user_input = input("Enter a number: ")
# value = eval(user_input)
# print(f"The value is {value} and its type is {type(value)}")

# changing variables type dynanmiclly
# x = 5
# print(type(x))
# x = "hello"
# print(type(x))
# x = 3.12
# print(type(x))

# text = "python"
# print(text[0])


# age = 19
# license = True

# if age >= 18:
#     if license:
#         print("your are eligible to drive")
#     else: 
#         print("you are not eligible to drive")
    
# age = 20 
# license = True 
# if age >= 18:
#     if license:
#         print("you are eligibel to drive")
# else:
#     print("you can not drive")

# age = 12
# license = True   # ← you must assign, NOT compare!

# if age >= 18:
#     if license:
#         print("you are eligible to drive")
# else:
#     print("you cannot drive")



# age = 17
# license = False

# if age >= 18:
#     if license:
#         print("you are eligible to drive")
#     else:
#         print("Make sure to get your license")
# else:
#     print("you are younger")
    
        


age = 20 
license = False
if age >= 18 and license:
    print("your are eligible to drive")
elif age <= 17:
    print("you are younger")
elif age >= 18 and license == False:
    print("you should get license")
else:
    print("you are not lega to drive")
