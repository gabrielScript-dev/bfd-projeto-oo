from view import View
from controller import Controller

view = View()
controller = Controller()


while True:
    opcao = view.exibir_menu()
    
    if opcao == '1':
        livro_in = view.view_adicionar_livro()
        resposta = controller.adicionar_livro(livro_in)
        view.exibir_msg(resposta)
    elif opcao == '2':
        escritor_in = view.view_adicionar_escritor()
        resposta = controller.adicionar_escritor(escritor_in)
        view.exibir_msg(resposta)
    elif opcao == '3':
        pass
    elif opcao == '4':
        pass
    elif opcao == '5':
        resposta = controller.listar_livros()
        view.exibir_msg(resposta)
    elif opcao == '6':
        exit()