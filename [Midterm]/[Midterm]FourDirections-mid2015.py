"""FourDirections"""
def line2(thiskey):
    """Print line2"""
    if thiskey == "L":
        print(" *   ", end=" ")
    elif thiskey == "R":
        print("   * ", end=" ")
    elif thiskey == "U":
        print(" *** ", end=" ")
    elif thiskey == "D":
        print("  *  ", end=" ")

def line3(thiskey):
    """Print line3"""
    if thiskey == "L":
        print("*****", end=" ")
    elif thiskey == "R":
        print("*****", end=" ")
    elif thiskey == "U":
        print("* * *", end=" ")
    elif thiskey == "D":
        print("* * *", end=" ")

def line4(thiskey):
    """Print line4"""
    if thiskey == "L":
        print(" *   ", end=" ")
    elif thiskey == "R":
        print("   * ", end=" ")
    elif thiskey == "U":
        print("  *  ", end=" ")
    elif thiskey == "D":
        print(" *** ", end=" ")

def main():
    """LEFT RIGHT UP DOWN"""
    arrow = str(input())
    num_ar = len(arrow)
    for i in range(1, 6, 1):
        if i == 1:
            for j in range(0, num_ar, 1):
                print("  *  ", end=" ")
        if i == 2:
            for j in range(0, num_ar, 1):
                thiskey = arrow[j]
                line2(thiskey)
        if i == 3:
            for j in range(0, num_ar, 1):
                thiskey = arrow[j]
                line3(thiskey)
        if i == 4:
            for j in range(0, num_ar, 1):
                thiskey = arrow[j]
                line4(thiskey)
        if i == 5:
            for j in range(0, num_ar, 1):
                print("  *  ", end=" ")
        print()
main()
