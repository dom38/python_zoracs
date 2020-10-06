# Print out the third letter in this variable:

tester = "PrintTheThirdLetter"
print(tester[2]) # <--- Put your answer in this print statement

# Sort this list alphabetically and then print it:

sortMe = ["Suna", "Freya", "Yuki", "Ichiro", "Ys", "Dogfart"]

sortMe.sort()

print(sortMe)

# Create a new file called big_dickheads.txt

file = open("big_dickheads.txt", mode="a")

# Write the above list to big_dickheads.txt

with open("big_dickheads.txt", mode="w") as file:
    for item in sortMe:
        file.write("%s\n" % item)

# Add the date to big_dickheads.txt WITHOUT overwriting the list already in there

import datetime

with open("big_dickheads.txt", mode="a") as file:
    file.write(str(datetime.datetime.now()))

# Create a function that adds together 1 to X, X being the argument for the function
# For example, function_name(5) would return "15", because 1+2+3+4+5 = 15
# function_name(3) would return 6, because 1+2+3 = 6

def my_function(X):
    return sum(range(X+1))

print(my_function(5))

# Create a function that takes 2 int arguments and returns 'true' if the first 
# number can be divided by the second number, and false otherwise. 
# eg. funcction_name(12, 6) returns true. funcction_name(12, 7) returns false. 
# As a tip, google 'python modulo operator'

def function_2(a, b):
    result = a%b
    if result == 0:
        print("true")
    else:
        print("false")

# Go to xiv_api.py, and see if you can get it to print JUST the slogan from the 
# get_fc_data function. For a second test, get it to print just the FC members 
# in alphabetical order from the get_fc_members function
# You WILL need to run `pip install requests` or `pip install -r requirements.txt`
