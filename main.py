import sys
import math

def validate_coefficient(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_coefficient_from_user(coefficient_name):
    while True:
        try:
            value = input(f"Введите коэффициент {coefficient_name}: ")
            return float(value)
        except ValueError:
            print(f"Ошибка! Коэффициент {coefficient_name} должен быть числом. Попробуйте еще раз.")

def parse_command_line_args():
    coefficients = []
    
    if len(sys.argv) >= 4:
        for i in range(1, 4):
            if validate_coefficient(sys.argv[i]):
                coefficients.append(float(sys.argv[i]))
            else:
                return None
        return coefficients
    return None

def solve_biquadratic(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен нулю для биквадратного уравнения!")
        return []
    
    D = b**2 - 4*a*c
    print(f"\nДискриминант D = {b}² - 4*{a}*{c} = {D}")
    
    roots = []
    
    if D > 0:
        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        print(f"t1 = {t1:.4f}, t2 = {t2:.4f}")
        
        if t1 > 0:
            x1 = math.sqrt(t1)
            x2 = -math.sqrt(t1)
            roots.extend([x1, x2])
            print(f"Корни из t1: x = ±{math.sqrt(t1):.4f}")
        elif t1 == 0:
            roots.append(0)
            print("Корень из t1: x = 0")
        
        if t2 > 0:
            x3 = math.sqrt(t2)
            x4 = -math.sqrt(t2)
            roots.extend([x3, x4])
            print(f"Корни из t2: x = ±{math.sqrt(t2):.4f}")
        elif t2 == 0 and 0 not in roots:
            roots.append(0)
            print("Корень из t2: x = 0")
            
    elif D == 0:
        t = -b / (2*a)
        print(f"t = {t:.4f}")
        
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            roots.extend([x1, x2])
            print(f"Два корня: x = ±{math.sqrt(t):.4f}")
        elif t == 0:
            roots.append(0)
            print("Один корень: x = 0")
        else:
            print("Нет действительных корней")
    else:
        print("Дискриминант отрицательный. Действительных корней нет.")
    
    return roots

def main():
    print("=" * 50)
    print("Решение биквадратного уравнения")
    print("Уравнение вида: A·x⁴ + B·x² + C = 0")
    print("=" * 50)
    
    coefficients = parse_command_line_args()
    
    if coefficients:
        a, b, c = coefficients
        print(f"\nКоэффициенты из командной строки:")
        print(f"A = {a}, B = {b}, C = {c}")
    else:
        print("\nВведите коэффициенты с клавиатуры:")
        a = get_coefficient_from_user("A")
        
        while a == 0:
            print("Коэффициент A не может быть равен 0 для биквадратного уравнения!")
            a = get_coefficient_from_user("A")
        
        b = get_coefficient_from_user("B")
        c = get_coefficient_from_user("C")
    
    print(f"\nРешаем уравнение: {a}·x⁴ + {b}·x² + {c} = 0")
    
    roots = solve_biquadratic(a, b, c)
    
    print("\n" + "=" * 50)
    if roots:
        unique_roots = []
        for root in roots:
            if root not in unique_roots:
                unique_roots.append(root)
        
        unique_roots.sort()
        
        print(f"Действительные корни: {len(unique_roots)}")
        for i, root in enumerate(unique_roots, 1):
            print(f"x{i} = {root:.6f}")
    else:
        print("Действительных корней нет")
    print("=" * 50)

if __name__ == "__main__":
    main()