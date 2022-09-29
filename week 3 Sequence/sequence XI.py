"""Sequence XI"""
def main():
    """print box of numbers"""
    size = int(input())
    for i in range(1, size+1):
        for j in range(1, i+1):
            print("%02d" %j, end=" ")

        for _ in range(-2*i+2*size, 0, -1):
            print("%02d" %i, end=' ')

        for k in reversed(range(1, i)):
            print("%02d" %(k), end=" ")
        print("")

    for re_i in range(size-1, 0, -1):
        for re_j in range(1, re_i+1):
            print("%02d" %re_j, end=" ")

        for _ in range(-2*re_i+2*size, 0, -1):
            print("%02d" %re_i, end=' ')

        for re_k in reversed(range(1, re_i)):
            print("%02d" %re_k, end=" ")
        print("")

#01    01 01 01 01 01 01 01 01
#01 02    02 02 02 02 02 02    01
#01 02 03    03 03 03 03    02 01
#01 02 03 04    04 04    03 02 01
#01 02 03 04 05       04 03 02 01

#01 02 03 04   04   04 03 02 01
#01 02 03   03 03 03   03 02 01
#01 02   02 02 02 02 02   02 01
#01   01 01 01 01 01 01 01   01
main()
