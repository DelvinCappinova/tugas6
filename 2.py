n = int(input("Input n nya: "))
for i in range(n, 0, -1):
    faktorial = 1
    for j in range(1, i+1):
        faktorial *= j

    print(faktorial, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()