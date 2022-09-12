"""forifball"""
def main():
    """forifball"""
    change = str(input())
    num1 = 1
    num2 = 2
    num3 = 3
    for i in range(0, len(change), 1):
        changeone = change[i]
        if changeone == "A":
            num1, num2 = num2, num1
        elif changeone == "B":
            num2, num3 = num3, num2
        elif changeone == "C":
            num1, num3 = num3, num1
    if num1 == 1:
        print("1")
    elif num2 == 1:
        print("2")
    elif num3 == 1:
        print("3")
main()
