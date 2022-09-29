"""Triangle"""
def main():
    """Triangle"""
    num = int(input())
    space = 1
    print("  "*(num-1), end="")
    print("%02d" %num)
    for i in range(num-1, 0, -1):
        print("  "*(i - 1), end="")
        print("%02d" %i, end="")
        print("  "*((2*space)-1), end="")
        print("%02d" %i, end="")
        print()
        space += 1
main()
