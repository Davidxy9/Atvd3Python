numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(numero, "é múltiplo de 3 e de 5.")
elif numero % 3 == 0:
    print(numero, "é múltiplo de 3.")
elif numero % 5 == 0:
    print(numero, "é múltiplo de 5.")
else:
    print(numero, "não é múltiplo de 3 nem de 5.")
