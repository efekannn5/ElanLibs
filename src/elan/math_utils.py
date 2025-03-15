class math_utils:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        return a ** 0.5

    def cube_root(self, a):
        return a ** (1/3)

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
            
    # Çoklu sayı işlemleri
    def sum_all(self, *args):
        """
        İstediğiniz kadar sayıyı toplayın
        Örnek: sum_all(1, 2, 3, 4, 5) -> 15
        """
        return sum(args)
    
    def multiply_all(self, *args):
        """
        İstediğiniz kadar sayıyı çarpın
        Örnek: multiply_all(1, 2, 3, 4, 5) -> 120
        """
        result = 1
        for num in args:
            result *= num
        return result
    
    def average(self, *args):
        """
        Sayıların ortalamasını alır
        Örnek: average(1, 2, 3, 4, 5) -> 3.0
        """
        if not args:
            return 0
        return sum(args) / len(args)
    
    def max_value(self, *args):
        """
        En büyük sayıyı bulur
        Örnek: max_value(1, 5, 3, 9, 2) -> 9
        """
        if not args:
            return None
        return max(args)
    
    def min_value(self, *args):
        """
        En küçük sayıyı bulur
        Örnek: min_value(1, 5, 3, 9, 2) -> 1
        """
        if not args:
            return None
        return min(args)
    
    def range_value(self, *args):
        """
        En büyük ve en küçük sayı arasındaki farkı bulur
        Örnek: range_value(1, 5, 3, 9, 2) -> 8
        """
        if not args:
            return None
        return max(args) - min(args)
    
    def median(self, *args):
        """
        Sayıların medyanını bulur
        Örnek: median(1, 3, 5, 7, 9) -> 5
        Örnek: median(1, 3, 5, 7) -> 4.0
        """
        if not args:
            return None
        
        sorted_args = sorted(args)
        length = len(sorted_args)
        
        if length % 2 == 0:
            # Çift sayıda eleman varsa, ortadaki iki sayının ortalamasını al
            return (sorted_args[length//2 - 1] + sorted_args[length//2]) / 2
        else:
            # Tek sayıda eleman varsa, ortadaki sayıyı al
            return sorted_args[length//2]

if __name__ == "__main__":
    math_utils()
    
