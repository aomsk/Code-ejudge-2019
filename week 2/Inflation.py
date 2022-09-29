"""Inflation"""
def main():
    """Inflation"""
    price = float(input())
    year = int(input())
    val = int(price * 100)
    for _ in range(year):
        val = int(val * 10381) // 10000
    print("%d.%02d"%((val//100), (val % 100)))

main()