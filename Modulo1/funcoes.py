def saudacao(nome):
  print(f"Ola, {nome}!")

saudacao("Alice")
saudacao("Bob")

def quadrado(numero):
  return numero ** 2

resultado_quadrado = quadrado(5)
print(resultado_quadrado)

def soma(numero1, numero2):
  return numero1 + numero2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

print(f"A soma de {num1} e {num2} eh {soma(num1, num2)}")