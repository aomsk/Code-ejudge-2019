"""CoPrimeV1"""
def gcdv2(num_1, num_2):
    """GCD"""
    while num_2 > 0:
        num_1, num_2 = num_2, num_1%num_2
    return num_1

def main():
    """CoPrimeV1"""
    num_1 = int(input())
    num_2 = int(input())
    gcd = gcdv2(num_1, num_2)
    if gcd == 1:
        print("YES")
    else:
        print("NO")
    print(gcd)
main()