"""Median"""
def main():
    """Median"""
    import statistics
    lis = []
    num = int(input())
    for _ in range(num):
        num_1 = int(input())
        lis.append(num_1)
    print("%.1f"%statistics.median(lis))

main()