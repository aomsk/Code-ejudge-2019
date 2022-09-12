"""Difference"""
def main():
    """Difference"""
    num_m = int(input())
    num_n = int(input())
    lis_a = []
    lis_b = []
    for i in range(num_m):
        lis_a.append(int(input()))
    for i in range(num_n):
        lis_b.append(int(input()))
    ans = set(lis_a) - set(lis_b)
    total = sorted(ans)
    for i in total:
        print(i, end=" ")
main()