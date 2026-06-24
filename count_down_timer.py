# Mini Project 2 Count Down Timer : Print a countdown timer before something exciting happens
# like "launching" or "happy new year"
#  concept used: for loop, range(), and the time module.


import time


count = int(input("Enter the countdown: "))

for count in range(count, 0 , -1):
    print(count)
    time.sleep(2)
print("Happy New Year!!!")