def brokenFunction(number, string):
    return number + string

try:
    print(broken)
except TypeError:
    print("Please check the input types.")
except NameError:
    print("You are trying to print something that does not exist.")
except:
    print("...")

else:
    print("Great! You didn't fuck up.")
finally:
    print("The End.")