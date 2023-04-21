numero = int(input("Digite um número: "))
divisores = []

for i in range(1, numero+1):
    if numero % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print(numero, "é primo.")
    print("Divisores:", divisores)
else:
    print(numero, "não é primo.")
