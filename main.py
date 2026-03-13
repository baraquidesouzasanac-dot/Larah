"""
v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)
"""

"""
e = int(imput("Digite sua idade"))
if idade % 2 == 0:
    print("idade é par.")
else:
    print("A idade é ímpar.")
if idade > 17:
    print("Você é maior de idade.")
else
    print("Você é menor de idade.")
"""

"""
número1 = float(input("Digite a Nota: "))
número2 = float(input("Digite a Nota: "))
número3 = float(input("Digite a Nota: "))

media = (número1 + número2 + número3) / 3
print("A média aritmética é:",media) 

if media >= 7:
     print("Aprovado")
else:
     print("Reprovado")
"""
  
  
  #for i in range(100):
#    print(i)

#i  = 10
#while i != 0:
#    i = i - 1
#   print(i)

#print("Fim do processamento!")
"""
soma = 0
for i in range( 1, 101):
    soma += i

print("A soma dos números de 1 a 100 é:", soma)
 
 numero = int(input("Digite um número: "))
"""

"""
print(f"Tabuada do {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
 def dobro(num):
    return num * 2

numero = int(input("escreva um número:"))
resultado = dobro(numero)

print("o dobro é:", resultado)
 soma = 0
while True :
    num = int(input("Digite um número(0 para sair):"))
    if num == 0:
        break
    soma += num
print("Soma total: ", soma)
"""  
"""
peso = float(input("digite seu peso (kg): "))
altura = float(input("digite sua altura (m): "))

imc = peso / (altura ** 2)

print("seu imc é: {imc:.1f}")

if imc <= 18.5:
    print("abaixo do peso")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau 1")
elif imc <= 39.9:
    print("obesidade grau 2")
else: 
    print("obesidade grau 3")
"""
"""
senha = input("Digite a senha para acessar o portal da sedu:")

while senha != "1234":
    print("Senha incorreta digite novamente.")
    senha = input("Digite a senha novamente para acessar o portal da sedu:")

print("Bem-vindo ao portal da sedu !")
"""
"""
valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
else:
    valor_final = valor_compra

print(f"Valor final da compra: R$ {valor_final:.2f}")
"""