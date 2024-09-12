# 04-09-2024
# Estrutura de Dados
# Riquelmy Henrique Silva

# Gerenciamento de Histórico de Navegação


class HistoricoNavegacao:

    def __init__(self):
        self.no = 0
        self.historico = {}

    def visitar_pagina(self, url):
        self.historico[self.no] = url
        self.no += 1

    def voltar(self):
        self.no -= 1
        self.historico.pop(self.no)

    def exibir_historico(self):
        print("Histórico:")
        for no, url in self.historico.items():
            print(f"{no}: {url}")

    def pagina_atual(self):
        if self.no > 0:
            print(f"Página atual: {self.historico[self.no - 1]}")
        else:
            print("Nenhuma página visitada.")


nav = HistoricoNavegacao()

nav.visitar_pagina("https://www.youtube.com/")
nav.visitar_pagina("https://www.fatecjd.edu.br/portal/")
nav.visitar_pagina("https://github.com/riquelmyhsilva")
nav.pagina_atual()
nav.exibir_historico()
nav.voltar()
nav.pagina_atual()
nav.voltar()
nav.pagina_atual()
