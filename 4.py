numero = float(input("Digite um número: "))
intervaloInicial = float(input("Digite um intervalo inicial: "))
intervaloFinal = float(input("Digite um intervalo final: "))

if intervaloInicial <= numero <= intervaloFinal:
    print("Está no intervalo")
else:
    print("Está fora do intervalo")