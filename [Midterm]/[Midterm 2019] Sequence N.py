"""[Midterm 2019] N"""
def main():
    """[Midterm 2019] N"""
    num = int(input())
    for row in range(num):
        for col in range(num):
            if col == 0 or col == num - 1 or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()