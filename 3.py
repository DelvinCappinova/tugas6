def persegi():
    tinggi = int(input("Input tinggi nya: "))
    lebar = int(input("Input lebar nya: "))
    awal = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(awal, end=" ")
            awal += 1
        print()
persegi()