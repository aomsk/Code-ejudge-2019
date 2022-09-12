"""Missing number"""
def main():
    """find missing number"""
    lis = []
    count = int(input())
    while 1:
        num = int(input())
        if num == 0:
            break
        lis.append(num)

    lis.sort()
    for i in range(1, count+1):
        if i not in lis:
            print(i)

main()