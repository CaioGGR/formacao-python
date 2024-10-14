nome = "Caioba"

# deixa em caps lock
print(nome.upper())

# deixa em minuscula
print(nome.lower())

# mostra a letra em determinada posicao
print(nome[2]) # vai mostrar a letra "i"

# contar quantas letras tem na variavel str
print(nome.count("a"))

# mostrar a posicao da letra
print(nome.find("a"))

# converte a string em bytes
nome.encode()

# converte de volta
nome.encode().decode()

# substituir letra por outra 
print(nome.replace("b","a")) # substitui os b por a

# colocar algo entre cada letra
print("-".join(nome))

nome2 = "Caio Gabriel"

# dividir a string
print(nome2.split(" "))

# remover algo do comeco e/ou final 
print(nome.strip("C"))

# comeca com
print(nome.startswith("Ca"))

# existe 
print("Ca" in nome)

# nao existe
print("Ca" not in nome)