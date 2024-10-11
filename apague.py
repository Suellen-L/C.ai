import pymongo
import pymongo.errors
from conexao import conecta

def apaga():
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