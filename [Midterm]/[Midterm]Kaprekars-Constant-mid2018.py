"""kaprekar's"""
def bubble(num1, num2, num3, num4):
    """kaprekar's"""
    num1, num2, num3, num4 = int(num1), int(num2), int(num3), int(num4)
    if num2 >= num1:
        num1, num2, num3, num4 = num2, num1, num3, num4
    if num3 >= num2:
        num1, num2, num3, num4 = num1, num3, num2, num4
    if num4 >= num3:
        num1, num2, num3, num4 = num1, num2, num4, num3
    if num3 >= num2:
        num1, num2, num3, num4 = num1, num3, num2, num4
    if num2 >= num1:
        num1, num2, num3, num4 = num2, num1, num3, num4
    if num3 >= num2:
        num1, num2, num3, num4 = num1, num3, num2, num4
    return str(num1)+str(num2)+str(num3)+str(num4)

def main(num):
    """kaprekar's"""
    count = cal = 0
    num = bubble(num[0], num[1], num[2], num[3])
    while cal != "6174":
        cal = int(num)-int(num[::-1])
        cal = "%04d"%cal
        num = bubble(cal[0], cal[1], cal[2], cal[3])
        count += 1
    print(count)
main(input())
