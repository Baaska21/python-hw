def get_digit_sum(n):
    result = 0
    if n < 0:
        n = - n
    while n > 0:
        result += n % 10
        n //= 10
    return result


if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(get_digit_sum(n))
