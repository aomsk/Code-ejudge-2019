"""[Midterm 2019] Harshad Number"""
def main():
    """[Midterm 2019] Harshad Number"""
    for _ in range(10):
        num = abs(int(input()))
        n_text = check(str(num))
        if num == 0:
            print("No")
        elif num % n_text == 0:
            print("Yes")
        else:
            print("No")

def check(num_1):
    """check function"""
    score = 0
    for i in num_1:
        score += int(i)
    return score

main()