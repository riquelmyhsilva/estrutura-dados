lista = [1, 2, 4, 5, 7, 8, 10]

lista_pares_quadrado = [num**2 for num in lista if num % 2 == 0]

print(lista_pares_quadrado)

prefixos = ["in", "anti", "ante", "pos"]
sufixos = ["felizmente", "comum", "moderno", "paro"]

combinacoes = [prefixo + sufixo for prefixo in prefixos for sufixo in sufixos]

print(combinacoes)

a = [5, 2, 3, 4]
b = [2, 5, 3, 8]

con_a = set(a)
con_b = set(b)

con_c = con_a.union(con_b)

print(con_c)

string = "paralelepipedo"
dic = {}

for letra in string:
    dic[letra] = string.count(letra)

print(dic)
