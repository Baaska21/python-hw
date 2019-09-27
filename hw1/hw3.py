def is_power_of_two(n):
    if n < 0:
        return False
    while n > 2:
        if n % 2 == 0:
            n = n / 2
            if n == 2:
              return True  
        else:
            return False

if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(is_power_of_two(n))