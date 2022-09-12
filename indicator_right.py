"""Indicator_Right"""
def main():
    """print right > """
    wide = int(input()) #กว้าง
    heigh = int(input()) #สูง
    upper = heigh//2+1
    lower = heigh-upper
    for i in range(upper):
        print(" "*i + "*"*wide)
    for j in range(lower-1, -1, -1):
        print(" "*j + "*"*wide)

main()
