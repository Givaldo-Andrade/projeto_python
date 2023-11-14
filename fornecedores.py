from datetime import datetime
import os

# Junior e Saulo

class Fornecedor:
    def __init__(self, id: int, nome: str, telefone: str, endereco: str, data: str):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.data = data
    
class Fornecedores:
    def __init__(self):
        self.list_fornecedor = list()
        self.Total = 0

    def add(self, fornecedor: Fornecedor):
        self.list_fornecedor.append(fornecedor)
        return self.list_fornecedor
    
    def remover(self):
        os.system('cls')
        data_hoje = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        print(f'''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------
Data/Hora: {data_hoje}
--------------------------------------------

OPÇÃO - 2
Remover Fornecedor
--------------------------------------------
''')
        if len(self.list_fornecedor) > 0:
            idItem = int(input('''Informe o ID do FORNECEDOR que deseja deletar:
ID: '''))
            try:
                i = idItem - 1
                for fornecedor in self.list_fornecedor:
                    if fornecedor == self.list_fornecedor[i]:
                        item_del =f'''
-----------------------------------
|        DADOS DO FORNECEDOR      |
-----------------------------------
ID: {fornecedor.id}
Nome: {fornecedor.nome}
Telefone: {fornecedor.telefone}
Endereço: {fornecedor.endereco}
Data: {fornecedor.data}
----------------------------------
'''
                        break
                    
                del self.list_fornecedor[i]
                
                d = 0
                for d, fornecedor in enumerate(self.list_fornecedor):
                    fornecedor.id = d + 1
                    
                print(f'''{item_del}
Fornecedor Deletado com Sucesso.
''')
                               
            except:
                print("\nID Inválido.")
            
        else:
            print("Nenhum Registro para Deletar.\n")    
        
        input('Pressione ENTER para Voltar.')
    
    def imprimir(self):
        os.system('cls')
        data_hoje = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        print(f'''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------
Data/Hora: {data_hoje}
--------------------------------------------

OPÇÃO - 7
Ver Fornecedores
--------------------------------------------''')
        if len(self.list_fornecedor) == 0:
            print("\nNenhum fornecedor cadastrado.\n")
        else:
            print('''
-------------------------------------
|      REGISTRO - FORNECEDORES      |
--------------------------------------------------------------------------------------------------------------------------------------------''')
            for fornecedor in self.list_fornecedor:
                print(f'''ID: {fornecedor.id} | Nome: {fornecedor.nome} | Telefone: {fornecedor.telefone} | Endereço: {fornecedor.endereco} | Data: {fornecedor.data}
--------------------------------------------------------------------------------------------------------------------------------------------''')
        
        input("Pressione ENTER para voltar")
                    
    def insert(self):
        while True:
            os.system('cls')
            data_hoje = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            print(f'''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------
Data/Hora: {data_hoje}
--------------------------------------------

OPÇÃO - 1
Cadastrar Fornecedor
--------------------------------------------
''')
            n = len(self.list_fornecedor)
            id = n + 1   
            nome = input("Informe o nome: ")
            
            try:
                telefone = int(input("Informe o telefone: "))
                
            except:
                input('''\n<ERROR> Informe apenas números no telefone.
Pressione ENTER para voltar.''')
                break
            
            endereco = input("Informe o endereço: ")
            data = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            forn = Fornecedor(id=id, nome=nome, telefone=telefone, endereco=endereco, data=data) 
            self.add(forn)
            
            continuar = input("\nCadastro realizado. Deseja continuar [SIM/NÃO]? ").lower()
                
            if continuar in ["sim", "s"]:
                pass
            
            else:
                break
