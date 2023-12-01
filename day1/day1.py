
def a():
    with open("input.txt", "r") as fp:
        total = 0
        for line in fp.readlines():
            for c in line:
                if ord(c) >= ord("0") and ord(c) <= ord("9"):
                    total += 10 * int(c)
                    break
            
            for c in reversed(line):
                if ord(c) >= ord("0") and ord(c) <= ord("9"):
                    total += int(c)
                    break
                
        return total
    
def b():
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    longestDigit = 5

    with open("input.txt", "r") as fp:
        total = 0
    
        for line in fp.readlines():
            foundIdx = len(line)
            found = ""
            for digit in digits:
                test = line.find(digit, 0, min(foundIdx + longestDigit, len(line)))
                if test >= 0 and test < foundIdx:
                    foundIdx = test
                    found = digit
            total += 10 * digits[found]
            
            foundIdx = -1
            found = ""
            for digit in digits:
                test = line.rfind(digit, max(foundIdx + 1 - longestDigit, 0))
                if test > foundIdx:
                    foundIdx = test
                    found = digit
            total += digits[found]
                
        return total
    
print(a())
print(b())