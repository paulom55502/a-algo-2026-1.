class Paciente:
    def __init__(self, nome, dor):
        self.nome = nome
        self.dor = dor

    def __str__(self):
        return f"{self.nome} (Dor: {self.dor})"


class MaxHeap:
    def __init__(self):
        self.heap = []

    # Função para encontrar pai
    def pai(self, i):
        return (i - 1) // 2

    # Filho esquerdo
    def esquerda(self, i):
        return 2 * i + 1

    # Filho direito
    def direita(self, i):
        return 2 * i + 2

    # Troca elementos
    def trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Inserir paciente
    def inserir(self, paciente):
        self.heap.append(paciente)
        self.subir(len(self.heap) - 1)

    # Ajusta para cima
    def subir(self, i):
        while i > 0 and self.heap[self.pai(i)].dor < self.heap[i].dor:
            self.trocar(i, self.pai(i))
            i = self.pai(i)

    # Ajusta para baixo
    def descer(self, i):
        maior = i
        esq = self.esquerda(i)
        dir = self.direita(i)

        if esq < len(self.heap) and self.heap[esq].dor > self.heap[maior].dor:
            maior = esq

        if dir < len(self.heap) and self.heap[dir].dor > self.heap[maior].dor:
            maior = dir

        if maior != i:
            self.trocar(i, maior)
            self.descer(maior)

    # Remover paciente prioritário
    def atender_paciente(self):
        if len(self.heap) == 0:
            return None

        raiz = self.heap[0]
        ultimo = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = ultimo
            self.descer(0)

        return raiz

    # Increase Key
    def aumentar_prioridade(self, indice, nova_dor):
        if nova_dor < self.heap[indice].dor:
            print("A nova prioridade deve ser maior.")
            return

        self.heap[indice].dor = nova_dor
        self.subir(indice)

    # Decrease Key
    def diminuir_prioridade(self, indice, nova_dor):
        if nova_dor > self.heap[indice].dor:
            print("A nova prioridade deve ser menor.")
            return

        self.heap[indice].dor = nova_dor
        self.descer(indice)

    # Mostrar heap
    def mostrar(self):
        for paciente in self.heap:
            print(paciente)


# =========================
# TESTE DO SISTEMA
# =========================

fila = MaxHeap()

fila.inserir(Paciente("Joao", 5))
fila.inserir(Paciente("Maria", 9))
fila.inserir(Paciente("Carlos", 3))
fila.inserir(Paciente("Ana", 7))

print("Fila inicial:")
fila.mostrar()

print("\nAtendendo paciente prioritario:")
print(fila.atender_paciente())

print("\nFila apas atendimento:")
fila.mostrar()

print("\nAumentando prioridade do Carlos para 10:")
fila.aumentar_prioridade(2, 10)

fila.mostrar()

print("\nDiminuindo prioridade de Ana para 2:")
fila.diminuir_prioridade(1, 2)

fila.mostrar()