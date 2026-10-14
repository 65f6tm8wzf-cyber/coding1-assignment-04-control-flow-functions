def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: We would get printed 3 and 4. At first we go to the for loop, where any number that is bigger than one, so two and three (will be passed to add_one), will go to the add_one function. So the for loop will go over 1, 2, and 3vbut will only pass 2 and 3 to the add_one function, which will add one to it and return it.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: It will return 3, because we are saying in the return portion to add one to the value in the add_one function. Retrun funtion does not display anything on the screen, it just sends the value to where the function was called. Print on the other hand, displays a value on the screen but does not return it.