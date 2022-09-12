"""3nPlus1"""
def main():
    """3nPlus1"""
    while 1:
        num = int(input())
        if num == 0:
            break
        print(three_plus_one(num))

def three_plus_one(num):
    """find 3nplus1"""
    if num == 1:
        return 1
    elif num % 2 == 0:
        count = three_plus_one(num//2) + 1
    else:
        count = three_plus_one(3*num+1) + 1
    return count

main()