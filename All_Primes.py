"""All_Primes"""
def main():
    """All_Primes"""
    num = int(input())
    count = 0
    for i in range(1, num+1):
        count += check(i)
    print(count)

def check(number):
    """check primes number"""
    count_primes = 0
    for j in range(2, number):
        if number % j == 0:
            count_primes += 1
        else:
            count_primes += 0
    if number == 1:
        return 0
    elif count_primes > 0:
        return 0
    else:
        return 1

main()