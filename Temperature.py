"""Temperature"""
def main():
    """Temperature"""
    num_temper = float(input())
    kind_num_temper = input()
    kind_want = input()
    temper = tem_celsius(num_temper, kind_num_temper)
    print("%.2f"%temper_answer(temper, kind_want))
def tem_celsius(num_temper, kind_num_temper):
    """change temperature to celsius"""
    if kind_num_temper == "F":
        val_cel = (num_temper - 32) / (9/5)
    elif kind_num_temper == "K":
        val_cel = num_temper - 273.15
    elif kind_num_temper == "R":
        val_cel = (num_temper / (9/5)) - 273.15
    elif kind_num_temper == "C":
        val_cel = num_temper
    return val_cel
def temper_answer(val_cel, kind_want):
    """temperature Each type"""
    if kind_want == "F":
        ans = (val_cel * (9/5)) + 32
    elif kind_want == "K":
        ans = val_cel + 273.15
    elif kind_want == "R":
        ans = (val_cel +273.15) * (9/5)
    elif kind_want == "C":
        ans = val_cel
    return ans
main()
