def isNumber(chrValue):
    if chrValue >= '0' and chrValue <= '9':
        return True
    return False

# Write the definition and implementation of the strToint function here
def strToint(string):
    string2 = isNumber(string)
    if string2 == True and int(string) > 0:
        return int(string)
    else:
        return -1

###########################

inputString = input("")
result = strToint(inputString)
if result == -1:
    print(inputString, "is not a positive integer value")
else:
    print("Result =", result)