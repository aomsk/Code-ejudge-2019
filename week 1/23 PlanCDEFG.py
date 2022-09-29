"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    text = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_mx = function_mx(num_1, num_2, num_3)
    num_mn = function_mn(num_1, num_2, num_3)
    num_mid = (num_1 + num_2 + num_3) - (num_mx + num_mn)
    if text == "Ascend":
        print("%.2f, %.2f, %.2f"%(num_mn, num_mid, num_mx))
    elif text == "Descend":
        print("%.2f, %.2f, %.2f"%(num_mx, num_mid, num_mn))

def function_mx(num_1, num_2, num_3):
    """what is max!!"""
    if num_2 < num_1 > num_3:
        return num_1
    if num_1 < num_2 > num_3:
        return num_2
    return num_3

def function_mn(num_1, num_2, num_3):
    """what is min!!"""
    if num_2 > num_1 < num_3:
        return num_1
    if num_1 > num_2 < num_3:
        return num_2
    return num_3

main()