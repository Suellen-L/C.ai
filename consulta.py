import pymongo
import pymongo.errors
from conexao import conecta

def leUser():
    colecoes = conecta()  
    if colecoes is not None:
        colecaoU = colecoes["Leitor"] 

        procura = input("Qual nick está procurando: ")
        lendo = colecaoU.find_one({'nick': procura}) 
        if lendo:
            print("Aqui está: ", lendo)
        else:
            print("Nop")
    else:
        print("Não conecto")


def leLivro():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"] 

        livros = colecaoL.find({}, {"titulo": 1, "_id": 0})
        print("Livros cadastrados:")
        for livro in livros:
            print(livro["titulo"])

        procura = input("Qual Livro está procurando: ")
        lendo = colecaoL.find_one({'titulo': procura}) 
        if lendo:
            print("Aqui está: ", lendo)
        else:
            print("Nop")
    else:
        print("Não conecto")

def leReacao():
    colecoes = conecta()
    if colecoes is not None:
        colecaoI = colecoes["Reacao"] 

        procura = input("Qual interação está procurando: ")
        lendo = colecaoI.find_one({'tipo': procura}) 
        if lendo:
            print("Aqui está: ", lendo)
        else:
            print("Nop")
    else:
        print("Não conecto")

def contar():
    colecoes = conecta()
    if colecoes is not None:
        colecaoU = colecoes["Leitor"]
        colecaoL = colecoes["Blibioteca"]
        colecaoR = colecoes["Reacao"]

        quantidadeU = colecaoU.count_documents({})
        quantidadeL = colecaoL.count_documents({})
        quantidadeR = colecaoR.count_documents({})
        print(f"Leitores e/ou Autores: {quantidadeU}")
        print(f"Blibioteca: {quantidadeL}")
        print(f"Reações: {quantidadeR}")
    else:
        print("Não conecto")
