def is_self_dividing(n):
    a = n
    result = 0
    if n < 0:
        n = -n
    while a > 0:
        if n % 10 != 0:
            result = a % 10
            a //= 10
            if n % result != 0:
                return False
        else:
            return False
    return True

if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(is_self_dividing(n))