"""Grade III"""
def calculate(num):
    """grade"""
    score = 0
    if 95 <= num <= 100:
        score = 4
    elif 90 <= num < 95:
        score = 3.5
    elif 85 <= num < 90:
        score = 3
    elif 80 <= num < 85:
        score = 2.5
    elif 75 <= num < 80:
        score = 2
    elif 70 <= num < 75:
        score = 1.5
    elif 65 <= num < 70:
        score = 1
    elif 60 <= num < 65:
        score = 0.5
    elif 0 <= num < 60:
        score = 0
    return score

def main(num):
    """Main function"""
    point = 0
    for _ in range(num):
        count = calculate(float(input()))
        point = point + count
    point = int((point/num)*100) / 100
    print("%.2f"% point)

main(int(input()))