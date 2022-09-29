"""Gift III"""
def main():
    """Gift III"""
    gift = int(input())
    num_1 = 0
    num_2 = 0
    if gift > 0:
        for _ in range(1, gift+1):
            num = int(input())
            if num > num_1:
                if num_1 >= num_2:
                    num_2 = num_1
                    num_1 = num
            elif num < num_1:
                if num > num_2:
                    num_2 = num
        if num_2 == 0:
            print("Exit")
        else:
            print(num_2)
    else:
        print("Exit")

main()