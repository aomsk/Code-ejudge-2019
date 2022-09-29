"""key"""
def main():
    """key"""
    num = int(input())
    p_text = check_plus(str(num))
    m_text = check_multi(str(num))
    amount = p_text + m_text
    if len(str(amount)) > 4:
        print(str(amount)[1:5])
    elif int(amount) < 1000:
        print(int(amount) + 1000)
    else:
        print(amount)

def check_plus(count_num):
    """check function"""
    score = 0
    for i in count_num:
        score += int(i)
    return score

def check_multi(num_1):
    """check function"""
    lis = []
    lis.append(num_1[10:13])
    score = 0
    for i in lis:
        score = int(i)*10
    return score

main()