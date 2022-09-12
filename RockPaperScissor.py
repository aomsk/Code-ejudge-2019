"""RockPaperScissor"""
def total(draw, a_point, b_point):
    """RockPaperScissor"""
    if a_point == b_point and a_point != 0:
        draw_point = a_point
        print("DRAW %d"%draw_point)
    elif a_point == b_point and a_point == 0:
        draw_point = draw
        print("DRAW %d"%draw_point)
    elif a_point > b_point:
        print("A win %d-%d" %(a_point, b_point))
    elif a_point < b_point:
        print("B win %d-%d" %(b_point, a_point))
def main():
    """Win lose draw"""
    comp = str(input())
    r0und = len(comp)
    draw = 0
    a_point = 0
    b_point = 0
    for i in range(0, r0und, 2):
        nay_a = comp[i]
        nay_b = comp[i+1]
        if nay_a == "R" and nay_b == "R":
            draw += 1
        elif nay_a == "R" and nay_b == "S":
            a_point += 1
        elif nay_a == "R" and nay_b == "P":
            b_point += 1
        elif nay_a == "S" and nay_b == "S":
            draw += 1
        elif nay_a == "S" and nay_b == "P":
            a_point += 1
        elif nay_a == "S" and nay_b == "R":
            b_point += 1
        elif nay_a == "P" and nay_b == "P":
            draw += 1
        elif nay_a == "P" and nay_b == "R":
            a_point += 1
        elif nay_a == "P" and nay_b == "S":
            b_point += 1
    total(draw, a_point, b_point)
main()
