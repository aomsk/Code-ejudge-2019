"""Timing"""
def main():
    """Timing"""
    sec = int(input())
    day = sec//86400
    days = sec%86400
    hours = days//3600
    hours_s = days%3600
    minute = hours_s//60
    second = hours_s%60
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%0.4d:%0.2d:%0.2d:%0.2d"%(day, hours, minute, second))

main()