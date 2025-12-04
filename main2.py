class CoefficientValidator:
    
    def is_valid(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def get_valid_coefficient(self, name):
        while True:
            try:
                value = input(f"Введите коэффициент {name}: ")
                coefficient = float(value)
                if name == 'A' and coefficient == 0:
                    print("Коэффициент A не может быть равен 0!")
                    continue
                return coefficient
            except ValueError:
                print(f"Ошибка! Коэффициент {name} должен быть числом.")

class BiquadraticEquation:
    
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []
        self.discriminant = None
    
    def set_coefficients(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_discriminant(self):
        self.discriminant = self.b**2 - 4*self.a*self.c
        return self.discriminant
    
    def solve(self):
        if self.a == 0:
            raise ValueError("Коэффициент A не может быть равен нулю")
        
        self.calculate_discriminant()
        self.roots = []
        
        print(f"\nДискриминант D = {self.b}² - 4*{self.a}*{self.c} = {self.discriminant}")
        
        if self.discriminant > 0:
            import math
            t1 = (-self.b + math.sqrt(self.discriminant)) / (2*self.a)
            t2 = (-self.b - math.sqrt(self.discriminant)) / (2*self.a)
            print(f"t1 = {t1:.4f}, t2 = {t2:.4f}")
            
            self._add_roots_from_t(t1, "t1")
            self._add_roots_from_t(t2, "t2")
            
        elif self.discriminant == 0:
            t = -self.b / (2*self.a)
            print(f"t = {t:.4f}")
            self._add_roots_from_t(t, "t")
            
        else:
            print("Дискриминант отрицательный. Действительных корней нет.")
        
        return self.get_unique_roots()
    
    def _add_roots_from_t(self, t, t_name):
        import math
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            self.roots.extend([x1, x2])
            print(f"Корни из {t_name}: x = ±{math.sqrt(t):.4f}")
        elif t == 0:
            self.roots.append(0)
            print(f"Корень из {t_name}: x = 0")
    
    def get_unique_roots(self):
        unique_roots = []
        for root in self.roots:
            if root not in unique_roots:
                unique_roots.append(root)
        unique_roots.sort()
        return unique_roots
    
    def display_solution(self):
        print(f"\nРешаем уравнение: {self.a}·x⁴ + {self.b}·x² + {self.c} = 0")
        
        try:
            roots = self.solve()
            
            print("\n" + "=" * 50)
            if roots:
                print(f"Действительные корни: {len(roots)}")
                for i, root in enumerate(roots, 1):
                    print(f"x{i} = {root:.6f}")
            else:
                print("Действительных корней нет")
            print("=" * 50)
            
        except ValueError as e:
            print(f"Ошибка: {e}")

class EquationSolverApp:
    
    def __init__(self):
        self.equation = BiquadraticEquation()
        self.validator = CoefficientValidator()
    
    def parse_arguments(self):
        import sys
        if len(sys.argv) >= 4:
            args = sys.argv[1:4]
            if all(self.validator.is_valid(arg) for arg in args):
                coefficients = [float(arg) for arg in args]
                if coefficients[0] == 0:
                    print("Коэффициент A из командной строки равен 0, будет запрошен новый")
                    return None
                return coefficients
        return None
    
    def run(self):
        print("=" * 50)
        print("Решение биквадратного уранвения")
        print("Уравнение вида: A·x⁴ + B·x² + C = 0")
        print("=" * 50)
        
        coefficients = self.parse_arguments()
        
        if coefficients:
            a, b, c = coefficients
            print(f"\nКоэффициенты из командной строки:")
            print(f"A = {a}, B = {b}, C = {c}")
            self.equation.set_coefficients(a, b, c)
        else:
            print("\nВведите коэффициенты с клавиатуры:")
            a = self.validator.get_valid_coefficient('A')
            b = self.validator.get_valid_coefficient('B')
            c = self.validator.get_valid_coefficient('C')
            self.equation.set_coefficients(a, b, c)
        
        self.equation.display_solution()

def main():
    app = EquationSolverApp()
    app.run()

if __name__ == "__main__":
    main()