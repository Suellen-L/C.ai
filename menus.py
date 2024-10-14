import pymongo
import pymongo.errors
import conexao
import adicionar
import consulta
import atualizar
import apague

def menuCRUD():
    print("1-Adicionar novo usuário, livro ou reação.")
    print("2-Consultar informações específicas de um usuário, livro ou reação.")
    print("3-Atualizar dados de um usuário ou livro")
    print("4-Remover um usuário ou livro.")
    
    escolha = input(" ")

    if escolha == "1":
        novo = input("1-usuário 2-livro 3-reação.")
        if novo == "1":
            adicionar.inseriUser()
        elif novo == "2":
            adicionar.inseriLivro()
        elif novo == "3":
            adicionar.inseriReacao()

    elif escolha == "2":
        novo = input("1-usuário 2-livro 3-reação.")
        if novo == "1":
            consulta.leUser()
        elif novo == "2":
            consulta.leLivro()
        elif novo == "3":
            consulta.leReacao()

    elif escolha == "3":
        novo = input("1-usuário 2-livro.")
        if novo == "1":
            atualizar.atualizaUser()
        elif novo == "2":
            atualizar.atualizaLivro()

    elif escolha == "4":
        novo = input("1-usuário 2-livro.")
        if novo == "1":
            apague.apagaUser()
        elif novo == "2":
            apague.apagaLivro()
    else:
        print("Opção inválida.")

def menuAgregacao():
    print("1-Total de usuários, livros e interações.")
    print("2-Encontrar os 5 livros mais bem avaliados.")
    
    escolha = input(" ")

    if escolha == "1":
        consulta.contar()
    elif escolha == "2":
        atualizar.melhoresL()
    else:
        print("Opção inválida.")


def menuPrincipal():
    while True:
        print("\nMenu Principal:")
        print("1- Caso queria adicionar, consultar, atualizar ou remover")
        print("2- Para saber os melhores livros ou total de usuarios, livros e reações")
        print("3-Sair")
        
        escolha = input(" ")

        if escolha == "1":
            menuCRUD()
        elif escolha == "2":
            menuAgregacao()
        elif escolha == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
