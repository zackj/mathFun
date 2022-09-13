# Numeric Palindromer
# Takes a number >= 0 and adds its reverse until a palindrome number
# is generated.
#
# Written by Zack Jarrett for his favorite sister.
# www.zackswagon.com
# September 12, 2022

import sys
import getopt

class PalindromeModel:
    def __init__(self):
        self.startInt = None
        self.debug = False

    def __str__(self):
        description = 'Palindrome Object' + '\n' + \
            f'  debug: {self.debug}' + '\n' + \
            f'  startInt: {self.startInt}'
        return description


def parseAndValidateArgs(argv: list, model: PalindromeModel):
    helpString = "Palindromer! Makes palindromes from numbers!\n" + \
        "For instance 48+84=132, but that's not a palindrome, so " + \
        "repeat the process again until it does: 132+231=363, yay!\n" + \
        "Start number must be >= 0."
    usageString = "palindromer.py --start <startInteger> [--debug]"

    try:
        opts, args = getopt.getopt(
            argv, "", ["help", "start=", "debug"])
    except getopt.GetoptError as e:
        print(f'Could not parse arguments: {e}')
        print(usageString)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--help":
            print('=-'*10)
            print(helpString)
            print(usageString)
            print('=-'*10)
            return False
        elif opt == "--start":
            model.startInt = int(arg)
            if model.startInt <= 0:
                print(f'startInteger must be >= 0.')
                return False
        elif opt == "--debug":
            model.debug = True

    if model.startInt == None:
        print(f'A start value must be provided.')
        return False

    return True


def reverseNum(inNum):
    s = str(inNum)
    reversedNum = "".join(list(reversed(s)))
    return int(reversedNum)


def isPalindrome(inNum):
    s = str(inNum)
    reversedStr = str(reverseNum(inNum))
    return s == reversedStr


def main():
    model = PalindromeModel()

    if model.debug:
        print(model)

    if (parseAndValidateArgs(sys.argv[1:], model) == False):
        exit(1)

    accumulator = model.startInt
    cursor = 0

    if model.debug:
        print(f'Start value is {accumulator}')

    while (isPalindrome(accumulator) == False):
        cursor += 1
        reverseAccum = reverseNum(accumulator)
        accumulator += reverseAccum
        if model.debug:
            print(f"Iteration {cursor} result: {accumulator}")

    print(
        f"{cursor} iterations required to go from {model.startInt} to {accumulator}")

    exit(0)


if __name__ == "__main__":
    main()
