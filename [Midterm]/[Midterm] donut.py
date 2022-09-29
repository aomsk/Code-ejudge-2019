"""Donut"""
def main():
    """Donut"""
    num = int(input()) #price
    num2 = int(input()) #num_donut
    num3 = int(input()) #free
    num4 = int(input()) #need_donut
    pack = num4 // (num2 + num3)
    num4 = num4 % (num2 + num3)
    if num4 < num2:
        get = num4
        num_price = num4 * num
    if num4 >= num2:
        get = num2 + num3
        num_price = num2 * num
    get = get + pack * (num2 + num3)
    num_price = num_price + pack * num2 * num
    print(num_price, get)
main()