"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    total = 0
    for i in range(num, 0, -1):
        total += 1
        print(i, end=" ")
        if total % 7 == 0:
            print()

main()