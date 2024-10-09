import pymongo
import pymongo.errors
from conexao import conecta

def inseriUser():
    colecaoU = conecta()
    if colecaoU is not None:
        nome = input("qual o seu nick: ")
        email = input("qual o seu emeil: ")
        livrosLido = input(" ")
        livrosfavorito = input(" ")
        seguindo = input(" ")
        seguidores = input(" ")

        doc = {"nome": nome, "email": email, "livrosLido": livrosLido, "livrosFavorito": livrosfavorito, "seguindo": seguindo, "seguidores": seguidores}
        colocar = colecaoU.insert_one(doc)
        colocar

def inseriLivro():
    colecaoL = conecta()
    if colecaoL is not None:
        titulo = input("qual o seu nick: ")
        autor = input("qual o seu emeil: ")
        genero = input(" ")
        editora = input(" ")
        avaliacao = input(" ")

        doc = {"titulo": titulo, "autor": autor, "genero": genero, "editora": editora, "avaliacao": avaliacao}
        colocar = colecaoL.insert_one(doc)
        colocar

def inseriReacao():
    colecaoI = conecta()
    if colecaoI is not None:
        tipo = input("qual o seu nick: ")
        nome = input("qual o seu emeil: ")
        titulo = input(" ")
        data = input(" ")

        doc = {"tipo": tipo, "nome": nome, "titulo": titulo, "data": data}
        colocar = colecaoI.insert_one(doc)
        colocar