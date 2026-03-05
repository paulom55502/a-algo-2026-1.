import random
import time


def insertion_sort(lista):
   
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


def gerar_lista(tamanho):
  
    return [random.randint(0, 100000) for _ in range(tamanho)]


def medir_tempo(funcao, lista):
    
    inicio = time.time()
    funcao(lista)
    fim = time.time()

    return fim - inicio


def main():
    tamanhos = [1000, 5000, 10000, 20000, 50000]

    for n in tamanhos:
        print(f"\nTamanho da lista: {n}")

        lista = gerar_lista(n)

        lista_insertion = lista.copy()
        lista_sorted = lista.copy()

        tempo_insertion = medir_tempo(insertion_sort, lista_insertion)
        tempo_sorted = medir_tempo(sorted, lista_sorted)

        print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
        print(f"sorted() Python: {tempo_sorted:.6f} segundos")


if __name__ == "__main__":
    main()
