"""Timing"""
def main():
    """Timing"""
    sec = int(input())
    day = (sec/3600/24)
    hour = (sec/3600)%24
    minute = (sec%3600)/60
    second = sec%60
    print("%d %d %d %d"%(day, hour, minute, second))

main()