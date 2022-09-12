"""ClockHandsTouch"""
def main():
    """ClockHandsTouch"""
    hour = int(input())
    mins = int(input())
    if hour == 12:
        hour = 0
    if mins == 60:
        mins = 0
    check_mins = mins*6
    check_hour = (hour*30)+(mins*0.5)
    if abs(check_mins - check_hour) < 6 and check_mins < check_hour:
        print(True)
    elif check_hour == check_mins:
        print(True)
    else:
        print("False")
main()
