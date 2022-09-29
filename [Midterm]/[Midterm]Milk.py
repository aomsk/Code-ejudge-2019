"""MILK"""
def main():
    """MILK"""
    price = int(input())
    quan = int(input())
    free = int(input())
    money = int(input())
    bottle = money//price
    bottle_cap = bottle
    while bottle_cap >= quan and quan != 0:
        bottle += free
        bottle_cap += (free-quan)
    print(bottle)
main()
