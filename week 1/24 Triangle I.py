"""Triangle I"""
def main():
    """Triangle I"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_a = function_mn(num_1, num_2, num_3)
    num_c = function_mx(num_1, num_2, num_3)
    num_b = (num_1 + num_2 + num_3) - (num_a + num_c)

    if abs(num_c**2 - (num_a**2 + num_b**2)) <= 0.01:
        print("Yes")
    else:
        print("No")

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