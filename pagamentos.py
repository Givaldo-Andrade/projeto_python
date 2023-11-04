import os
from datetime import datetime
    
class Pagamento(object):
    def __init__(self, id: int, descricao: str, fornecedor: str, metodo: str, valor: float, valorTotal: float, data: str):
        self.id = id
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.metodo = metodo
        self.valor = valor
        self.valorTotal = valorTotal
        self.data = data
    
class Pagamentos(object):
    def __init__(self):
        self.list_pagamentos = list()
        self.Total = 0
        
    def add(self, pagamento: Pagamento):
        self.list_pagamentos.append(pagamento)
        return self.list_pagamentos
    
    def imprimir(self):
        os.system('cls')
        print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 9
Ver Transações de Pagamento
--------------------------------------------''')
        if len(self.list_pagamentos) == 0:
            print("\nNenhum pagamento cadastrado.\n")
        
        else:  
            for pagamento in self.list_pagamentos:
                print(f'''
----------------------------------
|      REGISTRO - PAGAMENTO      |
----------------------------------
ID: {pagamento.id}
Fornecedor: {pagamento.fornecedor}
Descrição: {pagamento.descricao}
Método de Pagamento: {pagamento.metodo}
Valor: R${pagamento.valor:.2f}
Data: {pagamento.data}
----------------------------------''')
            print(f"Valor Total: R${self.Total:.2f}\n")
            
        input("Pressione ENTER para voltar.")
    
    def remover(self):
        os.system('cls')
        print('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

OPÇÂO - 6
Remover Pagamentos
--------------------------------------------
''')
        if len(self.list_pagamentos) > 0:
            idItem = int(input('''Informe o ID do PAGAMENTO que deseja deletar:
ID: '''))
            try:
                i = idItem - 1
                for pagamento in self.list_pagamentos:
                    if pagamento == self.list_pagamentos[i]:
                        self.Total -= pagamento.valor
                        item_del = f'''
-----------------------------------
|        DADOS DO PAGAMENTO      |
-----------------------------------
ID: {pagamento.id}
Fornecedor: {pagamento.fornecedor}
Descrição: {pagamento.descricao}
Método de Pagamento: {pagamento.metodo}
Valor: R${pagamento.valor:.2f}
Data: {pagamento.data}
-----------------------------------
'''
                        break
                
                del self.list_pagamentos[i]
                
                d = 0
                for d, pagamento in enumerate(self.list_pagamentos):
                    pagamento.id = d + 1
                    
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

OPÇÂO - 5
Cadastrar Pagamentos
--------------------------------------------''')
            n = len(self.list_pagamentos)
            id = n + 1    
            descricao = input("\nInforme a descricao: ")
            fornecedor = input("Informe o nome do fornecedor: ")
            metodo = input("Informe o metodo de pagemento [PIX, Boleto, Cartão, Dinheiro]: ")
            
            try:
                valor = float(input("Informe o valor: R$"))
            except:
                input('''<ERROR> Informe apenas números no valor :(.
Pressione ENTER para voltar.''')
                break
                
            self.Total += valor
            data = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
            pag = Pagamento(id=id, descricao=descricao, fornecedor=fornecedor, metodo=metodo, valor=valor, valorTotal=self.Total, data=data) 
            self.add(pag)
            
            continuar = input("\nCadastro realizado. Deseja continuar [SIM/NÃO]? ").lower()
            
            if continuar in ["sim", "s"]:
                pass
            
            else:
                break
