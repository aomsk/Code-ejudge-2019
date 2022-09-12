"""AlmostMean"""
def main():
    """ happy psit """
    line = int(input())
    menu = {}
    loww = {}
    for _ in range(0, line):
        stu = input()
        num = stu.replace("\t", "")
        menu[num[:8]] = float(num[8:])
    mean = sum(menu.values())/line
    menunokey = sorted(menu, key=menu.get)
    for i in menunokey:
        loww[i] = abs(mean-float(menu.get(i)))
    print(min(loww, key=loww.get), end="\t")
    last = min(loww, key=loww.get)
    print(menu[last])
main()
