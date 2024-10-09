import pymongo
import pymongo.errors

def conecta():
    
    try:
        conexao=pymongo.MongoClient("mongodb+srv://Suellen-L:ESTRELAPOLAR0909@cluster0.hv0wo.mongodb.net/")
        banco=conexao["C.ai"]
        colecaoU=banco["leitor"]
        colecaoL=banco["bliblioteca"]
        colecaoI=banco["reacao"]
        return colecaoU, colecaoI, colecaoL
    except pymongo.errors.ConnectionFailure as e:
        print("não rola não ",e)
        return None