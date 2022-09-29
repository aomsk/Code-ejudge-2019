""" Restaurant """
def main():
    """Restaurant"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    dis = (aaa+ddd)*((100-ccc)/100)
    if aaa == bbb:
        aaa = aaa*((100-ccc)/100)
    if dis < aaa:
        print("Yes %.3f" %(abs(dis-aaa)))
    elif dis > aaa:
        print("No %.3f" %(abs(dis-aaa)))
    else:
        print("Yes")
main()
