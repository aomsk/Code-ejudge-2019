"""Duplicate I"""
def main():
    """Duplicate I"""
    num_m = int(input())
    num_n = int(input())
    lis_m = []
    lis_n = []
    count = 0
    for i in range(num_m):
        lis_m.append(int(input()))
    for i in range(num_n):
        lis_n.append(int(input()))
    ans = set(lis_m).intersection(set(lis_n))
    for i in reversed(sorted(ans)):
        print(i)
        count += 1
    if count == 0:
        print("Nope")

main()
