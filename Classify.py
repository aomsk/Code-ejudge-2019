"""Classify"""
def main():
    """Classify"""
    lst_id = []
    while 1:
        num_stu_id = input()
        if num_stu_id != "END":
            lst_id.append(num_stu_id[0:4])
        else:
            break
    lst_id.sort()
    num_id = ""
    for i in lst_id:
        if i != num_id:
            if i[0:2] == num_id[0:2]:
                num_id = i
                print("--", int(num_id[2:4]), lst_id.count(num_id))
            else:
                num_id = i
                print(num_id[0:2], int(num_id[2:4]), lst_id.count(num_id))
main()
