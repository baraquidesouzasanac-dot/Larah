class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcularSubtotal(self):
        return self.quantidade * self.preco
    
class gestaoEstoque:
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, produto):
        self.produtos.append(produto)
        print(f"Sucesso: {produto.nome} cadastrado.")

    def listarProdutos(self, produtos):
        print("\n--- RELATORIO DE INVENTÁRIO ---")
        for p in self.produtos:
            print( f"Item: {p.nome} - Quantidade: {p.quantidade} - Unitario: R$ {p.preco:.2f}")

    def obterValorTotalEstoque(self):
        total = sum(p.calcularSubtotal() for p in self.produtos)
        return total
    def listarEstoqueBaixo(self, limite=5):
        print(f"\n--- PRODUTOS DE ESTOQUE  {limite} ---")
        
        criticos = [p for p in self.produtos if p.quantidade < limite]
        if not criticos:
            print("Nenhum produto com estoque baixo.")
        
        for p in criticos:
            print(f"ALERTA: {p.nome} tem apenas {p.quantidade} unidades")
            
sistema = gestaoEstoque()

sistema.adicionarProduto(Produto("Mouse sem fio", 15, 89.90))
sistema.adicionarProduto(Produto("Monitor LED", 3, 1200.00))
sistema.adicionarProduto(Produto("CABO HDMI", 2, 45.00))
            
valorTotal = sistema.obterValorTotalEstoque()
print(f"\nPatrimônio total do estoque: R$ {valorTotal:,.2f}")

sistema.listarEstoqueBaixo(5)             
