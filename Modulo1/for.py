lista = {1, 2, 3, 4, 5}

for elemento in lista:
  print(elemento)

pessoa = {"nome": "Caio", "idade": 23, "cidade": "Rio de Janeiro"}

print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
  print(chave)

print("For utilizando dicionario - values")
for valores in pessoa.values():
  print(valores)

print("For utilizando dicionario - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0, 1, 2, 3, 4]
for numero in range(5):
  print(f"Número: {numero}")

print("Utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice in range (0, len(lista)): # ou seja, de 0 até o número de itens da lista
  print(f"Posição {indice}: {lista[indice]}")

print("\nFazendo isso utilizando o enumarate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"Posição {indice}: {valor}")