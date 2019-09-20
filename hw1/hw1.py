#Задача №1

def get_digit_sum(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

n = int(input("Insert the number: "))
print(get_digit_sum(n))
