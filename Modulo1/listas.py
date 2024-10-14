lista = [1, 2, 3, 4, 5, 6, 7]
#        0  1  2  3  4  5  6

# caso queira fazer um slice da lista ate um certo numero, vc precisa pegar a posicao dele e somar 1
print(f"Teste de lista {lista[1:6]}") # vai do 2 (posicao 1) ate o 6 (posicao 5 +1)
print(f"Teste de lista {lista[:6]}") # vai do 1 ate o 6 (posicao 5 +1)

lista.append(8) # coloca o 8 no final da lista
print(lista)

# descobrir a posicao do item da lista
print(lista.index(5))

# colocar um elemento em uma posicao especifica
lista.insert(1, "dois") # insere um elemento em uma posicao especifica
print(lista)

# remover um elemento em uma posicao especifica
lista.pop(1) # remove o "dois"
print(lista)

# remove um elemento com o valor pedido
lista.remove(8) # remove o elemento 8
print(lista)

# colocar a lista em ordem crescente (caso todos os itens sejam do mesmo tipo)
lista.sort()
print(lista)

# mostrar o ultimo elemento
print(lista[-1])
