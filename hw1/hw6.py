def get_largest_perimiter(L):
    p = 0
    l= len(L)
    for i in range(l-2):
        for j in range(i + 1, l-1):
            for k in range(j + 1, l):
                a = float(L[i])
                b = float(L[j])
                c = float(L[k])
                if a + b > c and a + c > b and b + c > a:
                    p = a + b + c
    if p == 0:
        return False
    else:
        return p
    
if __name__ == '__main__':
    n = str(input('Введите числа: '))
    L = n.split()
    print(get_largest_perimiter(L))
