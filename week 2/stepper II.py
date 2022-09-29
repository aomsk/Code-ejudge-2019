"""stepper ii"""
def main():
    """Loop"""
    num_1 = int(input())
    num_2 = int(input())
    if num_1 >= num_2:
        for i in range(num_1, num_2-1, -1):
            print(i)
    elif num_1 <= num_2:
        for i in range(num_1, num_2+1):
            print(i)

main()