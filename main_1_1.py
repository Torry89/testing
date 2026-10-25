def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    d = b**2-4*a*c
    return d

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a,b,c)
    if d == 0:
        x = -b / (2 * a)
    elif d > 0:
        x = (-b + d ** 0.5)/(2 * a)
        x = (-b - d ** 0.5) / (2 * a)
    else:
        x="корней нет"
    return x

if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))




