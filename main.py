import os
import fornecedores
import pagamentos
import contas

def menu_geral():
    pagamentos.Pagamentos()
    os.system('cls')
    print(f'''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

<1> Para Cadastrar Fornecedor
<2> Para Remover Fornecedor
<3> Para Cadastrar Contas
<4> Para Remover Contas
<5> Para Cadastrar Pagamentos
<6> Para Remover Pagamentos
<7> Ver Fornecedores
<8> Ver Transações de Contas
<9> Ver Transações de Pagamentos
<10> Sair
''')

if __name__ == '__main__':
    fornecedor = fornecedores.Fornecedores()
    #contas
    pagamento = pagamentos.Pagamentos()
    
    while True:
        menu_geral()
        try:
            menu_opcao = int(input("Informe a opcao desejada: "))
            
            if menu_opcao == 1:
                fornecedor.insert()
                
            elif menu_opcao == 2:
                fornecedor.remover()
            
            elif menu_opcao == 3:
                #script cadastrar contas
                pass
            
            elif menu_opcao == 4:
                # script contas remover
                pass
                
            elif menu_opcao == 5:
                pagamento.insert()
            
            elif menu_opcao == 6:
                pagamento.remover()
            
            elif menu_opcao == 7:
                fornecedor.imprimir()
                
            elif menu_opcao == 8:
                # script imprimir contas
                pass
                
            elif menu_opcao == 9:
                pagamento.imprimir()    
                
            elif menu_opcao == 10:
                sair = input("\nDeseja realmente sair [SIM/NÃO]? ").lower()
                
                if sair in ["sim", "s"]:
                    break
                
                else:
                    pass
                
            else:
                input("Opção inválida. Pressione ENTER para Voltar.")
                
        except:
            input('''
<ERROR> Só é premitido números :(.
Pressione ENTER para continuar...''')
            
    input('''
--------------------------------------------         
|  PROGRAMA DE CADASTRO DE CONTAS A PAGAR  |
--------------------------------------------

Finalizado com sucesso...

PRESSIONE ENTER PARA FECHAR.''')