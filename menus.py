import pymongo
import pymongo.errors
import conexao
import adicionar
import consulta
import atualizar
import apague

def menuCRUD():
    print("Operações CRUD:")
    print("1-Adicionar novo usuário, livro ou reação.")
    print("2-Consultar informações específicas de um usuário, livro ou reação.")
    print("3-Atualizar dados de um usuário ou livro")
    print("4-Remover um usuário ou livro.")
    
    escolha = input("Escolha uma opção (1-4): ")

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
            apague.apaga
        elif novo == "2":
            consulta.leLivro()
    else:
        print("Opção inválida.")

def menuAgregacao():
    print("Operações de Agregação:")
    print("1-Calcular o número total de usuários, livros e interações.")
    print("2-Encontrar os 5 livros mais bem avaliados.")
    print("3-Identificar os autores mais seguidos.")
    
    escolha = input("Escolha uma opção (1-3): ")

    if escolha == "1":
        # Chama função para calcular totais
        calcular_totais()
    elif escolha == "2":
        # Chama função para encontrar os 5 livros mais bem avaliados
        encontrar_melhores_livros()
    elif escolha == "3":
        # Chama função para identificar autores mais seguidos
        identificar_autores_seguidos()
    else:
        print("Opção inválida.")

def menuIndices():
    print("Operações de Índices:")
    print("1-Criar índice composto (livro, avaliação) para otimizar consultas.")
    print("2-Criar índice composto (usuário, seguindo) para otimizar consultas.")
    
    escolha = input("Escolha uma opção (1-2): ")

    if escolha == "1":
        # Chama função para criar índice para livro e avaliação
        criar_indice_livro_avaliacao()
    elif escolha == "2":
        # Chama função para criar índice para usuário e seguindo
        criar_indice_usuario_seguindo()
    else:
        print("Opção inválida.")

def menuPrincipal():
    while True:
        print("\nMenu Principal:")
        print("1-Operações CRUD")
        print("2-Operações de Agregação")
        print("3-Operações de Índices")
        print("4-Sair")
        
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            menuCRUD()
        elif escolha == "2":
            menuAgregacao()
        elif escolha == "3":
            menuIndices()
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
