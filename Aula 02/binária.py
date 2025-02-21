def busca_binaria(lista, numero):

    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        chute = lista[meio]

        if chute == numero:
            return meio
        if chute > numero:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return None


if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 22, 34, 54, 67, 87, 98, 102, 123, 145, 167, 189, 200]
    numero = 11
    resultado = busca_binaria(lista, numero)
    if resultado is not None:
        print(f"Número encontrado em {resultado} interações.")
    else:
        print("Número não encontado na interação.")