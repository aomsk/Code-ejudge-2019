"""GCD_N"""
def main():
    """GCD_N"""
    num = int(input())
    lis = []
    for ii in range(num):
        count = int(input())
    for i in range(1, count + 1):
        if count % i == 0:
            lis.append(i)
    print(lis)
main()
