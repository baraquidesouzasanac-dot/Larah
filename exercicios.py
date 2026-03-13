"""
v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)
"""
"""
v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)
número1 = float(input("Digite a Nota1: "))
número2 = float(input("Digite a Nota2: "))
número3 = float(input("Digite a Nota3: "))
media = (número1 + número2 + número3) / 3
print("A média aritmética é:",media)
"""

"""
v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)
"""
"""
v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)


v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é...:",v_soma)

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
for i in range(100):
   print(i)

i  = 10
while i != 0:
    i = i - 1
  print(i)

print("Fim do processamento!")
"""
"""
soma = 0
for i in range( 1, 101):
    soma += i

print("A soma dos números de 1 a 100 é:", soma)
 numero = int(input("Digite um número: "))

 Mostra a tabuada de 1 a 10
print(f"Tabuada do {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
      def dobro(num):
    return num * 2

numero = int(input("escreva um número:"))
resultado = dobro(numero)
"""
"""
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
def calcular_inss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
        imposto = (valor * taxa)
        return imposto
    
valor_nota = float(input("Digite o valor da nota:"))
print(calcular_inss(valor_nota))
"""
"""
produtos_baguncados = [ "iphone 13 ", " MACBOOK PRO ", " aIrPoDs Pro", " iPad mini ", " caixa de som ",]
 
def padronizar_texto(texto):
    texto = texto.strip()
    texto = texto.title()
    return texto
produtos_padronizados = []
for produtos in produtos_baguncados:
    produtos_padronizado = padronizar_texto(produtos)
    produtos_padronizados. append(produtos_padronizado)

print(produtos_padronizados)
"""
"""
def analisar_margem(fateramento, custo):
lucro = (faturamento - custo)
margem = ((lucro / faturamento))
if margem >= 0.3:
   return "Margem Saudável"
else:
   return "Margem Baixa"


valor_custo = float(input("Digite o valor do custo:"))
valor_faturamento = float(input("Digite o valor do Faturamento: "))
print(analisar_margem(valor_faturamento,valor_custo))
"""
""""
def converter_para_real(valor_em_dolares,cotacao_dolar):
    valor_em_real = (valor_em_dolares * cotacao_dolar)
    return valor_em_real 

def processar_lista_precos(lista_precos_dolar, contacao_dolar):
    for item in lista_precos_dolar:
        valor_reias = converter_para_real(item,cotacao_dolar)
        print(f"O item custa US${item} e em reias: R$ {valor_reais}")

precos_usd = [100, 50, 250]
cortacao = 5.20
processar_lista_precos(precos_usd,cotacao)
"""
