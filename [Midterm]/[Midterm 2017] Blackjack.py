"""[Midterm 2017] Blackjack"""
def main():
    """find Blackjack"""
    num = int(input())
    score = 0
    check_a = 0
    for _ in range(num):
        card = input()
        if card in "JQK":
            score += 10
        elif card == "A":
            score += 1
            check_a += 1
        else:
            score += int(card)
    if 21 - score >= 10 and check_a >= 1:
        score += 10
    print(score)
main()
