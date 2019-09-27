def is_beauty(n):
    result = 0
    if n < 0:
        n = - n
    while n > 0:
        result += n % 10
        n //= 10
    if n % result == 0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(is_beauty(n))

