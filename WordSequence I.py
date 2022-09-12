"""WordSequence I"""
def main():
    """WordSequence I"""
    text = input()
    length = len(text)
    for row in range(length):
        for col in range(row + 1):
            print(text[col], end="")
        print()
main()