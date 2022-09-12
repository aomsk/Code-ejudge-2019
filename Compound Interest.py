"""Compound Interest"""
def main():
    """Compound Interest"""
    money = int(input())
    interest = float(input())
    year = int(input())
    for _ in range(year):
        total = (money * interest)/100
        count_money = total + money
        money = count_money
    print("%.2f"%money)

main()