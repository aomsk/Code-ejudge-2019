"""Sequence VIII"""
def main():
    """Sequence VIII"""
    number = int(input())
    for j in range(1, number+1):
        print("   "*(number-j), end="")
        for i in range(1, j+1):
            print("%02d"%i, end=" ")
        print()

main()
