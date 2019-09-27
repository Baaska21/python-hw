def is_prime(n):
    for i in range(2,n):
        if n % (i) == 0:
            return False
    return True
    
if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(is_prime(n))