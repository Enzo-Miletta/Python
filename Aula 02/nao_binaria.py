def busca_linear(lista, numero):

    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return -1

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90 ,100, 110, 120, 130, 140, 150]
numero = 30
resultado = busca_linear(lista, numero)

if resultado != -1:
    print(f"Numero encontrado na interação {resultado}")
else:
    print("Numero não encontrado na interação")