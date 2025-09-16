# Criação de Class Escritor
class escritor():

##Construtor da Classe ou Inicializacao dos meus atributos
    def __init__(self,nome):
        self.nome = nome
    def __str__(self): # __str__ é usado para definir como o objeto será exibido como texto, quando for usarmos o print.
        return self.nome # O return é para retornar apenas o nome
    
#Criação de Class Livro    
class livro():

#Construtor da Classe ou Inicializacao dos meus atributos  
    def __init__(self,titulo,ano):
        self.titulo = titulo
        self.ano = ano
      
 #Como o objeto sera exibido       
    def __str__(self):
        return f"'{self.titulo}' ({self.ano})"

#Criando o objeto ou instancia    
escritor1 = escritor('Leonardo')  
livros = livro('a baleia branca', 2021)

print(f'temos o Escritor: {escritor1}, com sua obra {livros}')
