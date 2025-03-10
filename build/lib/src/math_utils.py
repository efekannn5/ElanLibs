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

    def square_root(self, a):
        return a ** 0.5

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

if __name__ == "__main__":
    math_utils()
    
