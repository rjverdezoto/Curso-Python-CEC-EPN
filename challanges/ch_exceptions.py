#challange with exceptions
def readint(promt, min, max):
    try:
        userInput = int(input(promt))
        assert userInput > min and userInput < max
    except ValueError:
        return "not an interger"
    except AssertionError:
        return "not within range"
    return userInput
        

v = readint("Enter a number from -10 to 10: ",-10,10)

print("The number is:",v)