"""Bill"""
def main():
    """Chack Bill"""
    price = int(input())
    service = 0.1*price
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price = price+service
    vat = 0.07*price
    price = price + vat
    print("%.2f"%price)

main()
