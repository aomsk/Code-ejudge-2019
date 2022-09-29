"""[Midterm 2016] Align"""
def main():
    """[Midterm 2016]"""
    import math as m
    num = int(input())
    order = input()
    text = input()
    count = num - (len(text))
    total = count / 2
    text_l = m.ceil(total)
    text_r = m.floor(total)
    if order == "left":
        print(text.ljust(num, " "))
    elif order == "right":
        print(text.rjust(num, " "))
    elif order == "center":
        print(" "*text_l + text + text_r*" ")

main()