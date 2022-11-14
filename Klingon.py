#entrada de dados
x = input('Escreva o texto em Klingon: ')
#separa as palavras do texto, tranformando a variavel 'x' em lista 'palavras'
palavras = x.split()
y = 0
p = 0
v = 0
v1 = 0
n = 0
l = 1
nb = 0
g = 0
alfa = ['k','b','w','r','q','d','n','f','x','j','m','l','v','h','t','c','g','z','p','s']
for i in palavras:
    lista = list(i)
    c = len(lista)
    u = lista[c-1]
    p1 = lista[0]
#preposição
    if c == 3:
        if "d" in lista:
            pass
        elif u == 'f' or u == 's' or u == 'w' or u == 'l' or u == 'k':
            pass
        else:
            p += 1
#verbos
    elif c >= 8: 
        if u == 'f' or u == 's' or u == 'w' or u == 'l' or u == 'k':
            v += 1
        elif p1 == 'f' or p1 == 's' or p1 == 'w' or p1 == 'l' or p1 == 'k':
            v1 += 1
#remover palavras repetidas
def remove_repetidos(palavras):
    palavras1 = []
    for num in palavras:
        if num not in palavras1:
            palavras1.append(num)
    return palavras1
palavras = remove_repetidos(palavras)
#lista 'palavras' em ordem alfabética klingon
alfabeto = "kbwrqdnfxjmlvhtcgzps"
a = palavras
b = sorted(a, key=lambda word: [alfabeto.index(c) for c in word])
#numeros bonitos
for i in b:
    lista1 = list(i)
    n = 0
    g = 0
    l = 1
    for i in lista1:
        g = alfa.index(i)*l
        n = n + g
        l =  l*20
    if n >= 440556:
        if (n % 3) == 0:
            nb += 1
#Saída de Dados
print(f'Números bonitos existentes: {nb}')
print(f'\nNúmero de preposições: {p}')
print(f'Número de verbos: {v}')
print(f'Numéro de verbos em primeira pessoa: {v1}')
print(f'\nLista de vocabulário: {" ".join(b)}')