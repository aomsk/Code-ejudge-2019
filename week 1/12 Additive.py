
"""Source code's docstring"""


def main():
    """Function's docstring"""
    import math as m

    value_tops = m.sin(m.radians(90))+(m.sin(m.radians(60))**2)
    value_bottoms = m.cos(m.radians(245**2))+(m.cos(m.radians(180)))
    print(value_tops/value_bottoms)
    print((m.factorial(16) * m.factorial(4)) / m.factorial(8))
    values = (((25 - 12)**2) + ((12 - 15)**2))**.5
    print((15+25) / values)
    print(m.log10(1234**4))
    value_top = (m.log(4234, 5)+m.log2(8191)+(71*(m.log10(156154))))
    value_bottom = m.log(777, 7) - m.log(888, 8) - m.log(999, 9)
    print(value_top/value_bottom)


main()