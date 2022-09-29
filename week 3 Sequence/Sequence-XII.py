"""PSIT HW"""
def sequnce(num):
    """Sequnce"""
    for i in range(-num+1, num):
        for j in range(-num+1, num):
            if abs(i) == abs(j):
                print("%02d"%(num), end=" ")
            elif abs(i)-abs(j) > 0:
                print("%02d"%(num-(abs(i)-abs(j))), end=" ")
            elif abs(j)-abs(i) > 0:
                print("%02d"%(num-(abs(j)-abs(i))), end=" ")
        print()
sequnce(int(input()))
