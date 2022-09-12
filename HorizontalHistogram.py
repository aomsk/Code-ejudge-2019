"""HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    word = input()
    letters = {}
    for i in word:
        if i not in letters:
            letters[i] = 1
        elif i in word:
            letters[i] += 1
    for j in sorted(letters, key=str.swapcase):
        print(j + " " + ":", end=" ")
        for ppp in range(1, int(letters[j]) + 1):
            if ppp % 5 != 0:
                print("-", end="")
            elif ppp == int(letters[j]) and ppp % 5 == 0:
                print("-", end="")
            else:
                print("-" + "|", end="")
        print()
main()
