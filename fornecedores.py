from datetime import datetime
import os

class Fornecedor:
    def __init__(self, id: int, nome: str, empresa: str, telefone: str, endereco: str, valor: float, valorTotal: float, data: str):
        self.id = id
        self.nome = nome
        self.empresa = empresa
        self.telefone = telefone
        self.endereco = endereco
        self.valor = valor
        self.valorTotal = valorTotal
        self.data = data
    
class Fornecedores:
    def __init__(self):
        self.list_fornecedor = list()
        self.Total = 0

    def add(self, fornecedor: Fornecedor):
        self.list_fornecedor.append(fornecedor)
        return self.list_fornecedor
    
    def remover(self):
        if len(self.list_fornecedor) > 0:
            idItem = int(input('''Informe o ID do FORNECEDOR que deseja deletar:
ID: '''))
            try:
                i = idItem - 1
                for fornecedor in self.list_fornecedor:
                    if fornecedor == self.list_fornecedor[i]:
                        self.Total -= fornecedor.valor
                        item_del =f'''
-----------------------------------
|        DADOS DO FORNECEDOR      |
-----------------------------------
ID: {fornecedor.id}
Nome: {fornecedor.nome}
Empresa: {fornecedor.empresa}
Telefone: {fornecedor.telefone}
Endereço: {fornecedor.endereco}
Valor: R${fornecedor.valor:.2f}
Data: {fornecedor.data}
----------------------------------
'''
                        break
                    
                del self.list_fornecedor[i]
                
                d = 0
                for d, fornecedor in enumerate(self.list_fornecedor):
                    fornecedor.id = d + 1
                    
                print(f'''{item_del}
Item Deletado com Sucesso.
''')
                               
            except:
                print("ID Inválido.")
            
        else:
            print("Nenhum Registro para Deletar.\n")    
        
        input('Pressione ENTER para Voltar.')
    
    def imprimir(self):
        os.system('cls')
        print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 7
Ver Fornecedores
--------------------------------------------''')
        if len(self.list_fornecedor) == 0:
            print("\nNenhum fornecedor cadastrado.\n")
        else:
            for fornecedor in self.list_fornecedor:
                print(f'''
-----------------------------------
|      REGISTRO - FORNECEDOR      |
-----------------------------------
ID: {fornecedor.id}
Nome: {fornecedor.nome}
Empresa: {fornecedor.empresa}
Telefone: {fornecedor.telefone}
Endereço: {fornecedor.endereco}
Valor: R${fornecedor.valor:.2f}
Data: {fornecedor.data}
-----------------------------------''')
            print(f"Valor Total: R${self.Total:.2f}\n")
        
        input("Pressione ENTER para voltar")
        
    def insert(self):
        while True:
            os.system('cls')
            print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 1
Cadastrar Fornecedor
--------------------------------------------
''')
            n = len(self.list_fornecedor)
            id = n + 1   
            nome = input("Informe o nome: ")
            empresa = input("Informe o nome da empresa: ")
            
            try:
                telefone = int(input("Informe o telefone: "))
            except:
                input('''\n<ERROR> Informe apenas números no telefone.
Pressione ENTER para voltar.''')
                break
            
            endereco = input("Informe o endereço: ")
            
            try:
                valor = float(input("Informe o valor: R$"))
            except:
                input('''<ERROR> Informe apenas números no valor.
Pressione ENTER para voltar.''')
                break
            
            self.Total += valor
            data = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
            forn = Fornecedor(id=id, nome=nome, empresa=empresa, telefone=telefone, endereco=endereco, valor=valor, valorTotal=self.Total, data=data) 
            self.add(forn)
            
            continuar = input("\nCadastro realizado. Deseja continuar [SIM/NÃO]? ").lower()
                
            if continuar in ["sim", "s"]:
                pass
            
            else:
                break
