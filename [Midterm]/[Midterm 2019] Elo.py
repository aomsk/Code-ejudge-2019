"""[Midterm 2019] Elo"""
def main():
    """[Midterm 2019] Elo"""
    num_ra = int(input())
    num_rb = int(input())
    text = input()
    total_ea = 1/(1+(10**((num_rb-num_ra)/400)))
    total_eb = 1/(1+(10**((num_ra-num_rb)/400)))
    if text == "A":
        print("%.2f"%total_ea)
    else:
        print("%.2f"%total_eb)

main()