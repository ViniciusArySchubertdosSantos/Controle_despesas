class Despesa:
    def __init__(self,descricao,categoria,valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor

class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def listar_despesas(self):
        if self.despesas:
            for index, despesa in enumerate(self.despesas,start=1):
                print("-"*30)
                print(f"{index}.Descricao: {despesa.descricao}")
                print(f"Categoria: {despesa.categoria}")
                print(f"Valor: R${despesa.valor}")
                print("-"*30)
        else:
            print("Nenhuma despesa foi cadastrada")

if __name__ == '__main__':
    controle=ControleDespesas()

    while True:
        print("1. Adicionar Despesas")
        print('2. Listar Despesas')
        print("3. Sair")
        opcao = input("Escolha uma opção")

        if opcao == '1':
            descricao = input("Qual a descrição do produto?")
            categoria = input("Qual a categoria do produto?")
            valor = input("Qual o valor do produto?")
            despesa = Despesa(descricao,categoria,valor)
            controle.adicionar_despesas(despesa)
            print("-"*30)
            print("Despesa adicionada com sucesso")
            print("-"*30)
            
            
        elif opcao == '2':
            print('lista de Produtos:')
            controle.listar_despesas()

        elif opcao == '3':
            print('Até a próxima')
            break
            
        else:
            print('Opção invalida, tente novamente')
