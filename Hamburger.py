"""Hamburger"""
def main():
    """Hamburger"""
    bread_up = int(input())
    bread_under = int(input())
    total = (bread_up + bread_under)*2
    print("|"*bread_up+("*"*total)+"|"*bread_under)

main()