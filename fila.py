class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.frente = None
        self.tras = None

    def esta_vazia(self):
        return self.frente is None

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.frente = novo_no
            self.tras = novo_no
        else:
            self.tras.proximo = novo_no
            self.tras = novo_no

    def dequeue(self):
        if self.esta_vazia():
            return None
        valor = self.frente.valor
        self.frente = self.frente.proximo
        if self.frente is None:
            self.tras = None
        return valor

    def ver_frente(self):
        if self.esta_vazia():
            return None
        return self.frente.valor


fila = Fila()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

print(fila.ver_frente())
print(fila.dequeue())
print(fila.ver_frente())
print(fila.dequeue())
print(fila.ver_frente())
print(fila.dequeue())
print(fila.ver_frente())
