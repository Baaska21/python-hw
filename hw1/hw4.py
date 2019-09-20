#Задача №4

def is_prime(n):
    
    for i in range(2,n):
        if n % (i) == 0:
            return False
        else:
            pass
    return True

n = int(input("Insert the number: "))
print(is_prime(n))