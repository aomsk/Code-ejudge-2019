"""Run Length Decoding"""
def main():
    """ Decode input """
    word = input()
    num = ""
    for i in word:
        if i.isdigit():
            num += str(i)
        if i.isalpha():
            print(i * int(num), end="")
            num = ""
main()
