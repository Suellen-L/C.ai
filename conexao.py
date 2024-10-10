import pymongo
import pymongo.errors

def conecta():
    
    try:
        conexao=pymongo.MongoClient("mongodb+srv://Suellen-L:ESTRELAPOLAR0909@cluster0.hv0wo.mongodb.net/")
        banco=conexao["C-ai"]
        colecaoU=banco["Leitor"]
        colecaoL=banco["Blibioteca"]
        colecaoI=banco["Reacao"]
        print("foi")
        return {"Leitor": colecaoU, "Blibioteca": colecaoL, "Reacao": colecaoI}    
    
    except pymongo.errors.ConnectionFailure as e:
        print("não rola não ",e)
        return None
    
conecta()