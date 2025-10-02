class Escritor:
    def __init__(self, nome, email, descricao):
        self.__nome = nome
        self.__email = email
        self.__descricao = descricao
    
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def email(self):
        return self.__email
        
    @property
    def descricao(self):
        return self.__descricao
        

class Livro:
    def __init__(self, nome, ano, escritor):
        self.__nome = nome
        self.__ano = ano
        self.__escritor = escritor
        
    def exibir_dados(self):
        return f'''
        NOME DO LIVRO: {self.nome}
        ANO: {self.ano}
        --
        ESCRITOR: {self.escritor.nome}
        EMAIL: {self.escritor.email}
        --
            \n
        '''
            
    @property
    def nome(self):
        return self.__nome
        
    @property
    def ano(self):
        return self.__ano
        
    @property
    def escritor(self):
        return self.__escritor