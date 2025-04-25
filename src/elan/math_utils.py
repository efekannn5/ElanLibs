class math_utils:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def topla(self, a, b):
        return self.add(a, b)

    def subtract(self, a, b):
        return a - b

    def cikar(self, a, b):
        return self.subtract(a, b)

    def multiply(self, a, b):
        return a * b

    def carp(self, a, b):
        return self.multiply(a, b)

    def divide(self, a, b):
        return a / b

    def bol(self, a, b):
        return self.divide(a, b)

    def power(self, a, b):
        return a ** b

    def us(self, a, b):
        return self.power(a, b)

    def square_root(self, a):
        return a ** 0.5

    def karekok(self, a):
        return self.square_root(a)

    def cube_root(self, a):
        return a ** (1/3)

    def kupkok(self, a):
        return self.cube_root(a)

    def square(self, a):
        return a * a

    def kare(self, a):
        return self.square(a)

    def cube(self, a):
        return a * a * a

    def kup(self, a):
        return self.cube(a)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def faktoriyel(self, n):
        return self.factorial(n)

    def sum_all(self, *args):
        """
        İstediğiniz kadar sayıyı toplayın
        Örnek: sum_all(1, 2, 3, 4, 5) -> 15
        """
        return sum(args)

    def tumunu_topla(self, *args):
        """
        İstediğiniz kadar sayıyı toplayın
        Örnek: tumunu_topla(1, 2, 3, 4, 5) -> 15
        """
        return self.sum_all(*args)

    def multiply_all(self, *args):
        """
        İstediğiniz kadar sayıyı çarpın
        Örnek: multiply_all(1, 2, 3, 4, 5) -> 120
        """
        result = 1
        for num in args:
            result *= num
        return result

    def tumunu_carp(self, *args):
        """
        İstediğiniz kadar sayıyı çarpın
        Örnek: tumunu_carp(1, 2, 3, 4, 5) -> 120
        """
        return self.multiply_all(*args)

    def average(self, *args):
        """
        Sayıların ortalamasını alır
        Örnek: average(1, 2, 3, 4, 5) -> 3.0
        """
        if not args:
            return 0
        return sum(args) / len(args)

    def ortalama(self, *args):
        """
        Sayıların ortalamasını alır
        Örnek: ortalama(1, 2, 3, 4, 5) -> 3.0
        """
        return self.average(*args)

    def max_value(self, *args):
        """
        En büyük sayıyı bulur
        Örnek: max_value(1, 5, 3, 9, 2) -> 9
        """
        if not args:
            return None
        return max(args)

    def en_buyuk_deger(self, *args):
        """
        En büyük sayıyı bulur
        Örnek: en_buyuk_deger(1, 5, 3, 9, 2) -> 9
        """
        return self.max_value(*args)

    def min_value(self, *args):
        """
        En küçük sayıyı bulur
        Örnek: min_value(1, 5, 3, 9, 2) -> 1
        """
        if not args:
            return None
        return min(args)

    def en_kucuk_deger(self, *args):
        """
        En küçük sayıyı bulur
        Örnek: en_kucuk_deger(1, 5, 3, 9, 2) -> 1
        """
        return self.min_value(*args)

    def range_value(self, *args):
        """
        En büyük ve en küçük sayı arasındaki farkı bulur
        Örnek: range_value(1, 5, 3, 9, 2) -> 8
        """
        if not args:
            return None
        return max(args) - min(args)

    def aralik_degeri(self, *args):
        """
        En büyük ve en küçük sayı arasındaki farkı bulur
        Örnek: aralik_degeri(1, 5, 3, 9, 2) -> 8
        """
        return self.range_value(*args)

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

    def medyan(self, *args):
        """
        Sayıların medyanını bulur
        Örnek: medyan(1, 3, 5, 7, 9) -> 5
        Örnek: medyan(1, 3, 5, 7) -> 4.0
        """
        return self.median(*args)

if __name__ == "__main__":
    math_utils()
    
