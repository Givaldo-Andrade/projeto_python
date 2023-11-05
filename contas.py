import os
from datetime import datetime, date

class Conta(object):
    def __init__(self, id: int, descricao: str, fornecedor: str, vencimento: str, valor: float, valorTotal: float, data: str, status: str):
        self.id = id
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.vencimento = vencimento
        self.valor = valor
        self.valorTotal = valorTotal
        self.data = data
        self.status = status
    
class Contas(object):
    def __init__(self):
        self.list_contas = list()
        self.Total = 0
        
    def add(self, conta: Conta):
        self.list_contas.append(conta)
        return self.list_contas
    
    def imprimir(self):
        os.system('cls')
        print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 8
Ver Transações de Conta
--------------------------------------------''')
        if len(self.list_contas) == 0:
            print("\nNenhuma conta cadastrada.\n")
        
        else:
            for conta in self.list_contas:
                print(f'''
----------------------------------
|        REGISTRO - CONTA        |
----------------------------------
ID: {conta.id}
Fornecedor: {conta.fornecedor}
Descrição: {conta.descricao}
Valor: R${conta.valor:.2f}
Data Emissao: {conta.data}
Data Vencimento: {conta.vencimento}
Status: {conta.status}
----------------------------------''')
            print(f"Valor Total: R${self.Total:.2f}\n")
            
        input("Pressione ENTER para voltar.")
    
    def remover(self):
        os.system('cls')
        print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 4
Remover Contas
--------------------------------------------
''')
        if len(self.list_contas) > 0:
            idItem = int(input('''Informe o ID da CONTA que deseja deletar:
ID: '''))
            try:
                i = idItem - 1   
                for conta in self.list_contas:                  
                    if conta == self.list_contas[i]:
                        self.Total -= conta.valor
                        item_del = f'''
-----------------------------------
|         DADOS DA CONTA          |
-----------------------------------
ID: {conta.id}
Descrição: {conta.descricao}
Fornecedor: {conta.fornecedor}
Vencimento: {conta.vencimento}
Valor: R${conta.valor:.2f}
Data: {conta.data}
Status: {conta.status}
-----------------------------------
'''
                        break
                
                del self.list_contas[i]
                
                d = 0
                for d, conta in enumerate(self.list_contas):
                    conta.id = d + 1
                    
                print(f'''{item_del}
Item Deletado com Sucesso.
''')
                
            except:
                print("\nID Inválido.")
            
        
        else:
            print("Nenhum Registro para Deletar.\n")    
        
        input('Pressione ENTER para Voltar.')
    
    def insert(self):            
        while True:
            os.system('cls')
            print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 3
Cadastrar Contas
--------------------------------------------''')
            n = len(self.list_contas)
            id = n + 1    
            descricao = input("\nInforme a descricao: ")
            fornecedor = input("Informe o nome do fornecedor: ")
            try:
                d, m, y = [int(i) for i in input("Informe a data de vencimento (DD/MM/AAAA): ").split('/')]
                vencimento = date(y, m, d)
                tempo = date.today()
        
                if tempo > vencimento:
                    status = 'Atrasado'
                    
                else:
                    status = 'Pendente'
                    
                vencimento = vencimento.strftime("%d/%m/%y")
            except:
                input('''\n<ERROR> Informe a data no formato correto :(.
Pressione ENTER para voltar.''')
                break
            
            try:
                valor = float(input("Informe o valor: R$"))
            except:
                input('''<ERROR> Informe apenas números no valor :(. 
Pressione ENTER para voltar.''')
                break
                
            self.Total += valor
            data = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
            cont = Conta(id=id, descricao=descricao, fornecedor=fornecedor, vencimento=vencimento, valor=valor, valorTotal=self.Total, data=data, status=status) 
            self.add(cont)
            
            continuar = input("\nCadastro realizado. Deseja continuar [SIM/NÃO]? ").lower()
            
            if continuar in ["sim", "s"]:
                pass
            
            else:
                break
