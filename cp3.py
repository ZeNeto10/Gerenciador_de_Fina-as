import datetime
import matplotlib.pyplot as plt
#Nesses imports acima eu adicionei duas bibliotecas para conseguir ter a finalidade do código,

class GerenciadorFinancas:
    def __init__(self, saldo_inicial=100000):
        self.saldo = saldo_inicial
        self.transacoes = []
        
# Aqui, eu criei uma classe chamada "GERENCIADORFINANCAS", que obviamente representa o sistema o qual foi pedido 
# de gerenciar finacas.Utilizei o construtor "__init__" para criar uma instância da classe contendo um saldo
# inicial de 100.000 R$ além de ter uma lista vazia para guardar transações.

    def adicionar_transacao(self, tipo, valor, categoria, data=None):
        if data is None:
            data = datetime.date.today()
        transacao = {"tipo": tipo, "valor": valor, "categoria": categoria, "data": data}
        self.transacoes.append(transacao)
        if tipo == "despesa":
            self.saldo -= valor
        else:
            self.saldo += valor
            
#De acordo com a def "adicionar_transação" você determina o tipo, o valor, a categoria e a data da transação.

    def visualizar_saldo(self):
        return self.saldo
# Essa def "Vizualizar_saldo" serve para verificar o seu saldo.

    def gerar_relatorio(self):
        for transacao in self.transacoes:
            print(f"Tipo: {transacao['tipo']}, Valor: {transacao['valor']}, Categoria: {transacao['categoria']}, Data: {transacao['data']}")
#Essa def "gerar_relatorio", gera um relatorio sobre as transações realizadas.
    def categorizar_transacoes(self):
        categorias = {}
        for transacao in self.transacoes:
            categoria = transacao["categoria"]
            if categoria in categorias:
                categorias[categoria].append(transacao)
            else:
                categorias[categoria] = [transacao]
        return categorias

#A def "Categorizar_transações" basicamente ele vai criar um dicionário no qual as chaves são na verdade as
# categoras e os valores são listas associadas as categorias.

    def criar_grafico(self, categorias):
        labels = categorias.keys()
        valores = [sum(transacao['valor'] for transacao in categorias[categoria]) for categoria in labels]
        plt.pie(valores, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
        
#Aqui a def "Criar_grafico" ele realiza um grafico para mostrar todos os aspectos que foram utilizados antes,
#ou seja, valores e tals, utilizei a biblioteca "matplotlib" para gerar o gráfico e utilizei a bilioteca "plt.show"
# para exibir,
        
gerenciador = GerenciadorFinancas()
gerenciador.adicionar_transacao("despesa", 15000, "Costureira")
gerenciador.adicionar_transacao("despesa", 15000, "Funcionários")
gerenciador.adicionar_transacao("despesa", 27000, "Roupas")
gerenciador.adicionar_transacao("despesa", 35000, "Aluguel")
gerenciador.adicionar_transacao("receita", 10000, "Venda de roupas")

print(f"Saldo atual: R${gerenciador.visualizar_saldo()}")
print("Relatório de Transações:")
gerenciador.gerar_relatorio()
categorias = gerenciador.categorizar_transacoes()
print("Transações categorizadas:")
print(categorias)
print("Gráfico de categorias:")
gerenciador.criar_grafico(categorias)

# E no final do código, fica as ações e informações para o código conseguir "rodar" todo o projeto.