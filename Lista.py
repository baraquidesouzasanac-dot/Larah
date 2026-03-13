"""
class Cachorro:
    def latir(self)
        print("Au Au")

meu_dog = Cachorro()
meu_dog.latir()
"""
"""
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


ret1 = Retangulo(5, 3)

print("Área do retângulo:", ret1.calcular_area())     
"""
"""
class Animal:
    def comer(self):
        print("Comendo...")


class Cachorro(Animal):
    def som(self):
        print("Late")


class Gato(Animal):
    def som(self):
        print("Mia")


class Passaro(Animal):
    def som(self):
        print("Canta")


ser = int(input("Escolha um animal:(1 - Cachorro, 2 - Gato, 3 - Passaro): "))
a1 = Animal()
if ser == 1:
    a1 = Cachorro()
    a1.som()
    a1.comer()
elif ser == 2:
    a1 = Gato()
    a1.som()
    a1.comer()
elif ser == 3:
    a1 = Passaro()
    a1.som()
    a1.comer()
else:
    print("Escolha invalida!")  


a1.som()
"""
class contaBancaria:
    def __init__(self, saldoInicial):
        self.__saldo = saldoInicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def retirar(self, valor):
        if valor > 0:
            self.__saldo -= valor

    def verSaldo(self):
        return self.__saldo


quantia = contaBancaria(0)

opcao = 1
valor = 0
while opcao != 0:
    opcao = int(input("Escolha uma opção(1-Depositar/2-Sacar/0-Sair): "))
    if opcao != 0:
        valor = float(input("Digite o valor: "))
        if opcao == 1:
            quantia.depositar(valor)
        if opcao == 2:
            if valor > quantia.verSaldo():
                print("Saldo insuficiente!")
            else:               
                quantia.retirar(valor)
    print("Saldo atualizado..:",f" {quantia.verSaldo():,.2f}")
