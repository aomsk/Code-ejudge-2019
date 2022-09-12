"""Binary"""
def main():
    """find binary"""
    num = int(input())
    lis = ""
    while 1:
        lis += (str(num % 2))
        num = num // 2
        if num == 0:
            break
    print(lis[::-1])

main()