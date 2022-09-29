"""PlanB"""
def main():
    """PlanB"""
    num = float(input())
    if num >= 450:
        return passed()
    else:
        return failed()

def passed():
    """pass"""
    print("Pass")
    print("Process is terminated")

def failed():
    """fail"""
    print("Fail")
    print("Process is terminated")

main()