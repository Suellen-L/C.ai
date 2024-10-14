import pymongo
import pymongo.errors
from conexao import conecta

def apagaUser():
    colecoes = conecta()
    if colecoes is not None:
        colecaoU = colecoes["Leitor"]

        nick = input("caso queira realmente apagar a sua conta digite o seu nick: ")
        apagando = {"nick": nick}
        apagou = colecaoU.delete_one(apagando)
        if apagou.deleted_count > 0:
                print(f"{apagou.deleted_count} jogou fora:")
        else:
            print("não jogou nada fora")

def apagaLivro():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"]

        titulo = input("Caso queira realmente apagar seu livro, digite o título: ")
        nick = input("Qual o seu nick: ")

        livro = colecaoL.find_one({"titulo": titulo})

        if livro:
            if livro.get("autor") == nick:
                apagou = colecaoL.delete_one({"titulo": titulo})
                if apagou.deleted_count > 0:
                    print(f"{apagou.deleted_count} livro apagado.")
                else:
                    print("Erro ao tentar apagar o livro.")
            else:
                print("Você não é o autor deste livro. Não pode apagá-lo.")
        else:
            print("Livro não encontrado.")
    else:
        print("Erro: Conexão com a coleção falhou.")
