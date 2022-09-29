"""Circular I"""
def main():
    """Circular I"""
    num_x1 = float(input())
    num_y1 = float(input())
    num = float(input())
    num_x2 = float(input())
    num_y2 = float(input())
    total = (((num_x1 - num_x2)**2) + ((num_y1 - num_y2)**2))**(1/2)
    if total <= num:
        print("Yes")
    else:
        print("No")

main()