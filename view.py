from os import system
from controller import Controller

class View():
    def __menu_opcoes(self):
        menu = '''
            Sistema de Cadastro de Livros
            
            1 - Cadastrar Livro
            2 - Cadastrar Escritor
            3 - Buscar Livro
            4 - Excluir Livro
            5 - Listar Livros
            6 - Sair
        '''

        return menu
        
    def view_exibir_menu(self):
        
        system('cls||clear')
        
        print(self.__menu_opcoes())
        
        opcao = input('\t\tInforme uma opção: ').strip()
        
        return opcao
    
    def view_adicionar_livro(self):
        
        system('cls||clear')
        
        nome_livro = input('Informe o nome do Livro: ').strip()
        ano_livro = input('Ano do Livro: ').strip()
        nome_escritor = input('Nome do Escritor(a): ').strip()
        
        livro = {
            'nome': nome_livro,
            'ano': ano_livro,
            'escritor': nome_escritor
        }
        
        return livro
    
    def view_adicionar_escritor(self):
        
        system('cls||clear')
        
        nome_escritor = input('Informe o nome do(a) Escritor(a): ').strip()
        email_escritor = input('Informe o email do(a) Escritor(a): ').strip()
        descricao_escritor = input('Informe uma descrição do(a) Escritor(a): ').strip()
        
        escritor = {
            'nome': nome_escritor,
            'email': email_escritor,
            'descricao': descricao_escritor
        }
        
        return escritor
    
    def view_buscar_livro(self):
        
        system('cls||clear')
        
        nome_livro = input('Informe o nome do livro: ').strip()
        
        return {'nome': nome_livro}
    
    def view_excluir_livro(self):
        
        system('cls||clear')
        
        nome_livro = input('Informe o nome do livro: ').strip()
        
        return {'nome': nome_livro}
    
    def exibir_msg(self, response):
        
        if 'status' in response.keys():
            
            msg = f'''
                STATUS: {response['status']}
                MENSAGEM: {response['msg']}
            '''
        else:
            msg = f'''
                MENSAGEM: {response['msg']}
                DATA: \n\n {response['data']}
            '''
        
        system('cls||clear')
        input(msg)
    