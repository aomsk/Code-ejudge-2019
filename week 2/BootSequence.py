"""BootSequence"""
def main():
    """BootSequence"""
    num = int(input())
    print(*[i for i in range(1, num+1)], sep="_")

main(