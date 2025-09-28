from model import Livro, Escritor

class Controller:
    def __init__(self):
        self.__livros = []
        self.__escritores = []
    
    def adicionar_livro(self, livro):
        nome_livro = livro['nome']
        ano_livro = livro['ano']
        nome_escritor = livro['escritor']

        escritor = self.buscar_escritor(nome_escritor)
        
        if not escritor:
            return {'status': False, 'msg': 'Será necessário cadastrar o escritor(a)!'}
        else: 
            livro = Livro(nome=nome_livro, ano=ano_livro, escritor=escritor)
            self.__livros.append(livro)
            return {'status': True, 'msg': 'Livro Cadastrado com sucesso!'}
    
    def buscar_livro(self, nome):
        pass
    
    def excluir_livro(self, nome):
        pass
    
    def listar_livros(self):
        if len(self.__livros) == 0:
            return {'msg': 'Nenhum livro cadastrado!', 'data': None}
        else:
            livros = ''
            
            for livro in self.__livros:
                livros += livro.exibir_dados()
                
            return {'msg': 'Livros encontrados', 'data': livros}
    
    def adicionar_escritor(self, escritor):
        nome_escritor = escritor['nome']
        email_escritor = escritor['email']
        descricao_escritor = escritor['descricao']
        
        escritor = Escritor(nome=nome_escritor, email=email_escritor, descricao=descricao_escritor)
        
        self.__escritores.append(escritor)
        
        return {'status': True, 'msg': 'Escritor(a) cadastrado com sucesso!'}
    
    def buscar_escritor(self, nome):
        for escritor in self.__escritores:
            if escritor.nome == nome:
                return escritor
        return None