def c_to_f(c):
    return c * (9 / 5) + 32

def f_to_c(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    c_temp = int(input("섭씨 입력: "))
    f_temp = int(input("화씨 입력: "))

    print(c_to_f(c_temp))
    print(f_to_c(f_temp))
