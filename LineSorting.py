"""LineSorting"""
def main():
    """LineSorting"""
    num = int(input())
    lis = list()
    for _ in range(num):
        text = input()
        lis.append(text)
    lis.sort(key=len)
    for i in lis:
        print(i)
main()
