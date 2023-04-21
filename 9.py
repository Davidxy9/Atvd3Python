numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 % numero2 == 0:
    print(numero1, "é divisível por", numero2)
else:
    print(numero1, "não é divisível por", numero2)
