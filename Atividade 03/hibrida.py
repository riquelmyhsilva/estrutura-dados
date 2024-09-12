class Hibrida:
    def __init__(self, modo):
        self.topo = None
        if modo not in ["pilha", "fila"]:
            print("Modo Invalido")
        self.modo = modo
        self.estrutura = []

    def inserir(self, valor):
        self.estrutura.append(valor)

    def remover(self):
        if self.vazia():
            return None
        if self.modo == "fila":
            return self.estrutura.pop(0)
        else:
            return self.estrutura.pop()

    def frente(self):
        if self.vazia():
            return None
        if self.modo == "fila":
            return self.estrutura[0]
        else:
            return self.estrutura[-1]

    def vazia(self):
        return len(self.estrutura) == 0


lifo = Hibrida(modo="pilha")
fifo = Hibrida(modo="fila")

lifo.inserir(1)
lifo.inserir(2)
lifo.inserir(3)
lifo.inserir(4)

fifo.inserir(1)
fifo.inserir(2)
fifo.inserir(3)
fifo.inserir(4)

print("fila", fifo.estrutura)
print("pilha", lifo.estrutura)

lifo.frente()
fifo.frente()

lifo.remover()
fifo.remover()

lifo.frente()
fifo.frente()
