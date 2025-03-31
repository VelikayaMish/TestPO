import cmath

def quadratic_function(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    
    # Вычисляем дискриминант
    d = b**2 - 4*a*c
    
    # Находим два корня
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    
    return x1, x2
