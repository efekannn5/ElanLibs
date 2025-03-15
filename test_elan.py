from elan import elan

# Elan sınıfını başlat
el = elan()

# Matematik işlemleri testi
print("Matematik işlemleri:")
print(f"5 + 3 = {el.math.add(5, 3)}")
print(f"5 - 3 = {el.math.subtract(5, 3)}")
print(f"5 * 3 = {el.math.multiply(5, 3)}")
print(f"5 / 3 = {el.math.divide(5, 3)}")
print(f"5! = {el.math.factorial(5)}")

# String işlemleri testi
print("\nString işlemleri:")
print(f"'Merhaba' tersi: {el.string.reverse('Merhaba')}")
print(f"'merhaba' büyük harf: {el.string.uppercase('merhaba')}")
print(f"'MERHABA' küçük harf: {el.string.lowercase('MERHABA')}")

# Liste işlemleri testi
print("\nListe işlemleri:")
print(f"[1, 2, 3] tersi: {el.list.reverse([1, 2, 3])}")
print(f"[3, 1, 2] sıralı: {el.list.sort([3, 1, 2])}")
print(f"[1, 2, 2, 3, 3, 4] benzersiz: {el.list.unique([1, 2, 2, 3, 3, 4])}") 