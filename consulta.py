import pymongo
import pymongo.errors
from conexao import conecta

def leUser():
    colecaoU = conecta()
    if colecaoU is not None:
        procura = input("Qual produto está procurando: ")
        lendo = colecaoU.find_one({'nick': procura})  # ajuste aqui
    if lendo:
        print("Aqui está: ", lendo)
    else:
        print("Nop")

def leLivro():
    colecaoL = conecta()
    if colecaoL is not None:
        procura = input("Qual produto está procurando: ")
        lendo = colecaoL.find_one({'titulo': procura})  # ajuste aqui
    if lendo:
        print("Aqui está: ", lendo)
    else:
        print("Nop")

def leReacao():
    colecaoI= conecta()
    if colecaoI is not None:
        procura = input("Qual produto está procurando: ")
        lendo = colecaoI.find_one({'titulo': procura})  # ajuste aqui
    if lendo:
        print("Aqui está: ", lendo)
    else:
        print("Nop")