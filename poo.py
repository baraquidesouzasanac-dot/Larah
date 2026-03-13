"""
class calcularDobro:
    def __init__(self, valor):
        self.valor = valor
    
    def calcularDobro(self):
        return self.valor * 2
    
numero = float(input("Digite um número: "))
calculadora = calcularDobro(numero)
dobro = calculadora.calcularDobro()
print("O dobro do número informado é:", dobro)
"""
"""
class carro:
    tipo = "Veículo"

    def __init__(self,marca,modelo,ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

c1 = carro("Toyota","Corolla",2025)
c2 = carro("Honda","City",2026)
c3 = carro("Hyundai","HB20",2024)

for x in (c1,c2,c3):
    print(x.marca,x.modelo,x.ano,x.tipo,)
"""    
"""
class Pessoa:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Estudante(Pessoa):
    pass


p = Pessoa("José", "Silva")
p.printname()
s = Estudante("Ana", "Beatriz")
s.printname()
"""
"""
class Pessoa:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario 

p1 = Pessoa("Larah", 1000)
print(p1.nome)
print(p1.salario)
"""

"""
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def __validacao(self, numero):
        if not isinstance(numero, (int, float)):
            return False 
       else:
            return  True 
    def adicionar(self, numero):
        if self.__validacao(numero):
            self.resultado += numero
        else:
            print("Número INVÁLIDO")

calc = Calculadora()
calc.adicionar("A")
calc.adicionar("B")
print(calc.resultado) 
"""
"""
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
       
livro1 = Livro("O pequeno principe", "Antoine de Saint-Exupéry")
livro1.exibir_info()
print("Título do livro:", livro1.titulo, "escrito por:", livro1.autor)
"""
