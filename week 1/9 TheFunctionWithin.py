"""TheFunctionWithin"""
def main():
    """TheFunctionWithin"""
    num_a, num_b, num_c, num_d = float(input()), float(input()), float(input()), float(input())
    print(func_f(func_f(num_a)))
    print(func_g(func_f(num_a - num_b)))
    print(func_h(func_f(num_a + num_b), func_f(num_a + num_c), func_g(func_f(num_d**2))))
    print(func_i(func_h(func_f(num_a + num_b), func_f(num_a - num_c), func_g(func_f(num_d**2)))\
    , func_g(func_f(num_a - num_b)), func_f(func_f(func_f(func_f(func_f(num_c))))), num_d**8))

def func_f(num_x):
    """func f"""
    return 2*num_x

def func_g(num_x):
    """func g"""
    return 3*num_x**4-num_x**3+2*num_x**2+10

def func_h(num_x, num_y, num_z):
    """func h"""
    return (num_z + num_x)**2-num_x*num_y+num_y**2

def func_i(num_a, num_b, num_c, num_d):
    """func i"""
    return (num_a**2+num_b**2-num_c**2)/(num_d**2-2*num_a*num_d+2*num_a)

main()