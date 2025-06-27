def get_real_floor(n: int) -> int:

    if n >= 14:
        real_floor = n-2
    elif n <= 0:
        real_floor = n
    else:
        real_floor = n-1

    return real_floor


if __name__ == "__main__":
    print(get_real_floor(10))
    print(get_real_floor(15))
    print(get_real_floor(0))
    print(get_real_floor(-6))
