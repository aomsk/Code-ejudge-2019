"""CoinChangev1"""
def main():
    """CoinChangev1"""
    money = int(input())
    coins = [25, 10, 5, 1]
    total = 0
    for coin in coins:
        total += money//coin
        money = money%coin
    print(total)
main()
