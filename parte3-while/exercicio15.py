num = 1
par = 0
impar = 0
while num != 0:
    num = float(input("Digite um número: "))
    if num%2 == 0:
        par = par + 1
    else:
        impar = impar + 1
par=par - 1
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")