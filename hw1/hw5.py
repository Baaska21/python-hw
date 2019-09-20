#Задача №5

def is_self_dividing(n):
    a = n
    result = 0
    while a > 0:
        result = a % 10
        a //= 10
        if n % result == 0:
            pass
        else:
            return False
    return True

n = int(input("Insert the number: "))
print(is_self_dividing(n))