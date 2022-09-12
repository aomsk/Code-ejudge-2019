"""Heads and Legs"""
def main():
    """Heads and Legs"""
    heads = int(input())
    legs = int(input())
    rabbits, ghost = divmod(legs - 2*heads, 2)
    birds = heads - rabbits
    if rabbits >= 0 and birds >= 0 and ghost == 0:
        print(rabbits, birds)
    else:
        print('Impossible')

main()
