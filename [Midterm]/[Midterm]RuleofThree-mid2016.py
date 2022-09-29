"""RuleofThree"""
def main():
    """RuleofThree"""
    rund = int(input())
    savep = float(input())
    savew = float(input())
    best_value = savew/savep
    best_p, best_w = savep, savew
    for _ in range(0, rund-1, 1):
        price = float(input())
        weight = float(input())
        value = weight/price
        if value > best_value or (value == best_value and price < best_p):
            best_value = value
            best_p, best_w = price, weight
    print("%.2f %.2f"%(best_p, best_w))
main()
