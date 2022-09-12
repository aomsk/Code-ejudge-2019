"""Seeker"""
def main():
    """Seeker"""
    text = input()
    count = ''
    state = 0
    lis = []
    total = 0
    for i in text:
        if i.isdigit():
            count += i
            state = 1
        else:
            if state == 1:
                lis.append(count)
                count = ''
                state = 0
    if text[-1].isdigit():
        lis.append(count)
    name = list(map(int, lis))
    for i in name:
        total += i
    print(total)
main()