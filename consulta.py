import pymongo
import pymongo.errors
from conexao import conecta

def le():
    colecaoU = conecta()
    if colecaoU is not None:
        procura = input("Qual produto está procurando: ")
        lendo = colecaoU.find_one({'tipo': procura})  # ajuste aqui
    if lendo:
        print("Aqui está: ", lendo)
    else:
        print("Nop")
