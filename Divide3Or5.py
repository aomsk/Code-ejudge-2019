"""Divide3Or5"""
def main():
    """Divide3Or5"""
    num = int(input())
    score = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            score += i
    print(score)

main()
