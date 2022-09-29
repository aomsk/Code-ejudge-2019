"""Sequence X"""
def main(num_1):
    """find sequence X"""
    space = num_1*3 - 3
    num = 1
    while space > -1:
        for i in range(1, num + 1):
            if i == 1:
                print(" "*space + "%02d"%i, end=" ")
            elif i != num:
                print("%02d"%i, end=" ")
            else:
                print("%02d"%i, end=" ")
                num_2 = num
                for j in range(num_2 - 1, 0, -1):
                    print("%02d"%j, end=" ")
        print()
        space -= 3
        num += 1
    space = 3
    num = num_1 - 1
    while space <= num_1*3 - 3:
        for i in range(1, num + 1):
            if i == 1:
                print(" "*space + "%02d"%i, end=" ")
            elif i != num:
                print("%02d"%i, end=" ")
            else:
                print("%02d"%i, end=" ")
                num_3 = num
                for j in range(num_3 - 1, 0, -1):
                    print("%02d"%j, end=" ")
        print()
        space += 3
        num -= 1
main(int(input()))
