"""[Final 2019 Recommend] Guess"""
def guess(text):
    """answer"""
    op, num, ans = text.split()
    if op == ">" and ans == "YES":
        return set(range(int(num)+1, 101))
    elif op == ">" and ans == "NO":
        return set(range(0, int(num)+1))
    elif op == "<" and ans == "YES":
        return set(range(0, int(num)))
    elif op == "<" and ans == "NO":
        return set(range(int(num), 101))
    elif op == "=" and ans =="YES":
        return set([int(num)])
    else:
        return set(range(101)) - set([int(num)])

def main():
    """[Final 2019 Recommend] Guess"""
    answer = set(range(0, 101))
    while 1:
        text = input()
        if text == "END":
            break
        newset = guess(text)
        answer = answer.intersection(newset)
    answer = sorted(list(answer))
    print(*answer)

main()
