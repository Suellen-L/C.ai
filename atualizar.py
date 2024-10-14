import pymongo
import pymongo.errors
from conexao import conecta

def atualizaUser():
    colecoes = conecta()
    if colecoes is not None:
        colecaoU = colecoes["Leitor"]

        nick = input("qual o nick que tera atualização: ")
        email = input("se for alterar o email, qual o novo: ")
        livrosLido = input("qual o livro acabou de ser lido: ")
        livrosFavorito = input("quais os seus livros favoritos: ")
        seguindo = input("qual o nick do leitor que deseja seguir: ")

        adicioane = {}
        if email.strip():
            adicioane["email"] = email
        if livrosLido.strip():
            adicioane["livrosLido"] = {"$push": livrosLido} 
        if livrosFavorito.strip():
            adicioane["livrosFavorito"] = {"$push": livrosFavorito}
        if seguindo.strip():
            adicioane["seguindo"] = {"$push": seguindo}

        foi = colecaoU.update_one({"nick": nick}, {"$set": adicioane})        
        if foi.matched_count > 0:
            print(f"{foi.modified_count} documentos atualizados.")
        else:
            print("Não rolo")

def atualizaLivro():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"]

        titulo = input("qual o livro quer avaliar: ")
        avaliacao = float(input("deixe uma avaliação para o livro de 1 a 5: "))

        adicioane = {}
        if avaliacao:
            adicioane["avaliacao"] = {"$push": avaliacao} 
        foi = colecaoL.update_one({"titulo": titulo}, {"$push": adicioane})
        
        if foi.matched_count > 0:
            print(f"{foi.modified_count} documentos atualizados.")
        else:
            print("Não rolo")

def melhoresL():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"]

        livros = colecaoL.find({"avaliacoes": {"$exists": True, "$ne": []}})
        mediaL = []

        for livro in livros:
            somaA = sum(livro["avaliacoes"])
            totalA = len(livro["avaliacoes"])
            mediaA = somaA / totalA
            mediaL.append({"titulo": livro["titulo"], "media_avaliacoes": mediaA, "total_avaliacoes": totalA})

        mediaL.sort(key=lambda x: x["media_avaliacoes"], reverse=True)

        melhores_livros = mediaL[:5]

        if melhores_livros:
            print("Os 5 melhores livros são:")
            for livro in melhores_livros:
                print(f"Titulo do livro: {livro['titulo']}, Média das avaliações: {livro['media_avaliacoes']:.2f}, Total de avaliações: {livro['total_avaliacoes']}")
        else:
            print("Sem avaliações por aqui")


