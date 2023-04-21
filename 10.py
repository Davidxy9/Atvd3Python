numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é primo.")
            break
    else:
        print(numero, "é primo.")
else:
    print("O número precisa ser maior que 1 para ser primo.")
