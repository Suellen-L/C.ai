import pymongo
import pymongo.errors
from conexao import conecta

def inseriUser():
    colecoes = conecta()
    if colecoes is not None:
        colecaoU = colecoes["Leitor"] 

        nick = input("qual o seu nick: ")
        email = input("qual o seu emeil: ")
        livrosLido = input(" ")
        livrosfavorito = input(" ")
        seguindo = input(" ")
        seguidores = input(" ")

        doc = {"nick": nick, "email": email, "livrosLido": livrosLido, "livrosFavorito": livrosfavorito, "seguindo": seguindo, "seguidores": seguidores}
        try:
            colocar = colecaoU.insert_one(doc)
            print(f"Leitor adicionado, seu ID e: {colocar.inserted_id}")
        except Exception as e:
            print(f"Leitor não adicionado: {e}")
    else:
        print("Erro: Conexão com a coleção falhou.")


def inseriLivro():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"] 

        titulo = input("qual o nome do livro: ")
        autor = input("quem escreveu este livro: ")
        genero = input("qual o genero desse livro: ")
        editora = input("qual a editora publicou o livro: ")
        avaliacao = input(" ")

        doc = {"titulo": titulo, "autor": autor, "genero": genero, "editora": editora, "avaliacao": avaliacao}
        try:
            colocar = colecaoL.insert_one(doc)
            print(f"Livro adicionado, o ID e: {colocar.inserted_id}")
        except Exception as e:
            print(f"Livro não adicionado: {e}")
    else:
        print("Erro: Conexão com a coleção falhou.")

def inseriReacao():
    colecoes = conecta()
    if colecoes is not None:
        colecaoI = colecoes["Reacao"] 

        tipo = input("sera qual interação? [curtir, comentar, compartilhar]: ")
        if tipo == 'comentar':
            interacao = input("qual o seu comentario: ")
        else:
            interacao = None 
        nick = input("qual o seu nick: ")
        titulo = input("qual o nome do livro: ")
        data = input("qual a data de hoje: ")

        doc = {"tipo": tipo, "interacao":interacao, "nick": nick, "titulo": titulo, "data": data}
        try:
            colocar = colecaoI.insert_one(doc)
            print(f"Reação adicionado, seu ID e: {colocar.inserted_id}")
        except Exception as e:
            print(f"Reação não adicionado: {e}")
    else:
        print("Erro: Conexão com a coleção falhou.")
