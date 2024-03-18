def prima(angka):
    if angka <= 1:
        return False
    if angka == 2:
        return True
    if angka % 2 == 0:
        return False
    for i in range(3, int(angka**0.5) + 1, 2):
        if angka % i == 0:
            return False
    return True

def ganjil_prima_tertinggi(n):
    for i in range(n - 1, 1, -1):
        if prima(i):
            return i
        
angka = int(input("Masukkan angka : "))
prima = ganjil_prima_tertinggi(angka)
print(f"Prima terdekat dari {angka} adalah {prima}")
