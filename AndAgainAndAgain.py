"""Again"""
def main():
    """print"""
    list_ans = []
    total = 0
    check = 0
    text = input().split(" ")
    for i in text:
        if i.count("a") > 0:
            total += i.count("a")
        if i.count("e") > 0:
            total += i.count("e")
        if i.count("i") > 0:
            total += i.count("i")
        if i.count("o") > 0:
            total += i.count("o")
        if i.count("u") > 0:
            total += i.count("u")
        if total == 1:
            total = 0
        if total > 1:
            list_ans.append(i)
            total = 0
            check += 1
    list_ans.sort()
    for i in list_ans:
        print(i.replace(".", ""))
    if check == 0:
        print("Nope")
main()
