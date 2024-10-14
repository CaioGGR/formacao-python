pessoa = {"nome": "Caio", "idade": 23, "cidade": "Rio de Janeiro"}

print("Meu dicionario", pessoa)

print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Ribeiro"
print("Sobrenome:", pessoa["sobrenome"])

print("Meu dicionario", pessoa)

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionario apos remocao", pessoa)

#Metodos: keys(), values(), items()
#keys
chaves = list(pessoa.keys())
print("Chaves:", chaves)
print("Selecionando primeira chave:", chaves[0])

# Metodo values
valores = list(pessoa.values())
print("Valores:", valores)
print("Selecionando primeiro valor:", valores[0])

# Metodo items que retorna tuplas com pares de chave-valor
itens = list(pessoa.items())
print("pares de chave-valor: ", itens)
print("primeira chave-valor: ", itens[0][0], itens[0][1])
