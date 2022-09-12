"""Fever"""
def main():
    """Fever"""
    cel = float(input())
    if cel == 36 or cel < 38:
        print("No Fever")
    elif cel == 38 or cel < 39:
        print("Mild Fever")
    elif cel == 39 or cel < 40:
        print("High Fever")
    elif cel == 40 or cel <= 43:
        print("Very High Fever")

main()
