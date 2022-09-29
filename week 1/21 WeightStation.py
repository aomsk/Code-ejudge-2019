"""WeightStation"""
def main():
    """WeightStation"""
    avg = float(input())
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_4 = (avg*4) - (num_1 + num_2 +num_3)
    total_all = num_1 + num_2 + num_3 + num_4
    avg_2 = avg/2
    if total_all > 15000:
        return print("Overweight")
    if abs(num_1 - avg) > avg_2:
        print("Unbalance")
    elif abs(num_2 - avg) > avg_2:
        print("Unbalance")
    elif abs(num_3 - avg) > avg_2:
        print("Unbalance")
    elif abs(num_4 - avg) > avg_2:
        print("Unbalance")
    else:
        print("Pass %.2f"%(num_4))

main()