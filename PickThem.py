"""LastStand"""
import json
def main():
    """find LastStand"""
    num = json.loads(input())
    count = 0
    for i in num:
        if i%2 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")

main()