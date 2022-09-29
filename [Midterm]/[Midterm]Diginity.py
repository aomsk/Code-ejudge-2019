"""DIGINITY"""
def caltoone(idnumber, cal_id):
    """DIGINITY"""
    num = 0
    cal_id = len(idnumber)
    for i in range(0, cal_id, 1):
        thiscol = int(idnumber[i])
        num += thiscol
    cal_id = len(str(num))
    idnumber = str(num)
    if cal_id != 1:
        caltoone(idnumber, cal_id)
    elif cal_id == 1:
        print(num)

def main():
    """THIS IS MAIN FUNCTION"""
    while True:
        idnumber = str(input())
        if idnumber == "0":
            break
        cal_id = len(idnumber)
        if cal_id == 1:
            num = int(idnumber)
            print(num)
        else:
            caltoone(idnumber, cal_id)
main()
