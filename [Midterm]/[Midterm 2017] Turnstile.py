"""Turnstile"""
def main():
    """Turnstilemain"""
    act = "locked"
    data_c = 0
    while 1:
        data = input()
        if data == "END":
            break
        if act == "locked":
            if data == "P":
                act = "locked"
            elif data == "C":
                act = "unlocked"
        if act == "unlocked":
            if data == "C":
                act = "unlocked"
            elif data == "P":
                act = "locked"
                data_c += 1
    print(data_c)
main()