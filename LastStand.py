"""LastStand"""
import json
def main():
    """LastStand"""
    num = json.loads(input())
    for i in num:
        num_1 = i%10
        print(num_1)

main()