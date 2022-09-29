"""Circular II"""
def main():
    """Circular II"""
    num_xme = float(input())
    num_yme = float(input())
    radi_me = float(input())
    num_xf = float(input())
    num_yf = float(input())
    radi_f = float(input())
    result = ((num_xme - num_xf)**2 + (num_yme - num_yf)**2)**0.5
    total = radi_me + radi_f
    if total > result:
        print("Yes")
    else:
        print("No")

main()