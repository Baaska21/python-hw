#Задача №2

def get_digit_sum(n):
    global result
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

def is_beauty(result, n):
    if n % result == 0:
        return True
    else:
        return False
    

n = int(input("Insert the number: "))
print(get_digit_sum(n))
print(is_beauty(result, n))

