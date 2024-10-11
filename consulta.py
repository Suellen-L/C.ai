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
        print("Erro: Conexão com a coleção falhou.")

leUser()

def leLivro():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"] 

        procura = input("Qual Livro está procurando: ")
        lendo = colecaoL.find_one({'titulo': procura}) 
        if lendo:
            print("Aqui está: ", lendo)
        else:
            print("Nop")
    else:
        print("Erro: Conexão com a coleção falhou.")

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
        print("Erro: Conexão com a coleção falhou.")
leReacao()