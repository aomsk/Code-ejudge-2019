"""OddEvenFighting"""
def main():
    """OddEvenFighting"""
    even = 0
    odd = 0
    while 1:
        num = int(input())
        if num == 0:
            break
        if num%2 == 0:
            even += num
        if num%2 != 0:
            odd += num
    if even > odd:
        print("Even", even)
    elif odd > even:
        print("Odd", odd)
    else:
        print("Draw", even)

main()
