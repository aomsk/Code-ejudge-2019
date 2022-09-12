"""isprime_small"""
def main():
    """isprime_small"""
    num = int(input())
    if num == 1 or num == 0:
        print("No")
    else:
        for i in range(2, num):
            if num%i == 0:
                print("No")
                break
        else:
            print("Yes")

main()