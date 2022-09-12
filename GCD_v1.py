"""GCDv1"""
def main():
    """GCDv1"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    lis = []
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        print(num_1)
    else:
        for i in range(1, min(num_1, num_2, num_3)+1):
            if num_1 % i == 0 and num_2 % i == 0 and num_3 % i == 0:
                lis.append(i)
        print(max(lis))

main()