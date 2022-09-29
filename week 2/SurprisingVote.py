"""SurprisingVote"""
def main():
    """SurprisingVote"""
    point_all = float(input())
    point_mx = float(input())
    count = point_all - point_mx if point_all - point_mx < point_mx else point_mx
    reasult = point_all-(point_mx+count)
    if point_mx - reasult > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()