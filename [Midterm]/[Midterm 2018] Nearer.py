"""[Midterm 2018] Nearer"""
def main():
    """[Midterm 2018]"""
    alice = int(input())
    bob = int(input())
    itim = int(input())
    distance_1 = abs(itim - alice)
    distance_2 = abs(itim - bob)
    if distance_1 < distance_2:
        print("Alice %d"%distance_1)
    elif distance_2 < distance_1:
        print("Bob %d"%distance_2)
    elif distance_1 == distance_2:
        print("Sundaes %d"%distance_1)

main()
