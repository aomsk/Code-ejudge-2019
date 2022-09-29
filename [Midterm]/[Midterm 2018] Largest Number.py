"""[Midterm 2018] Largest Number"""
def main(num1, num2, num3):
    """[Midterm 2018}"""
    cn1 = int(num1+num2+num3)
    cn2 = int(num1+num3+num2)
    cn3 = int(num2+num1+num3)
    cn4 = int(num2+num3+num1)
    cn5 = int(num3+num1+num2)
    cn6 = int(num3+num2+num1)
    print(check(check(check(check(check(cn1, cn2), cn3), cn4), cn5), cn6))

def check(ch1, ch2):
    """check"""
    if ch1 > ch2:
        return ch1
    else:
        return ch2

main(input(), input(), input())