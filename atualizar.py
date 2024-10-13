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
        if email:
            adicioane["email"] = {"$set": email} 
        if livrosLido:
            adicioane["livrosLido"] = {"$push": livrosLido} 
        if livrosFavorito:
            adicioane["livrosFavorito"] = {"$push": livrosFavorito}
        if seguindo:
            adicioane["seguindo"] = {"$push": seguindo}

        foi = colecaoU.update_one({"nick": nick}, {"$push": adicioane})
        
        if foi.matched_count > 0:
            print(f"{foi.modified_count} documentos atualizados.")
        else:
            print("Nenhuma alteração realizada.")

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
            print("Nenhuma alteração realizada.")

def melhoresL():
    colecoes = conecta()
    if colecoes is not None:
        colecaoL = colecoes["Blibioteca"]

        livros = colecaoL.find({"avaliacoes": {"$exists": True, "$ne": []}})
        livros_com_media = []

        for livro in livros:
            soma_avaliacoes = sum(livro["avaliacoes"])
            total_avaliacoes = len(livro["avaliacoes"])
            media_avaliacoes = soma_avaliacoes / total_avaliacoes
            livros_com_media.append({
                "titulo": livro["titulo"],
                "media_avaliacoes": media_avaliacoes,
                "total_avaliacoes": total_avaliacoes
            })

        livros_com_media.sort(key=lambda x: x["media_avaliacoes"], reverse=True)

        melhores_livros = livros_com_media[:5]

        if melhores_livros:
            print("Os 5 melhores livros são:")
            for livro in melhores_livros:
                print(f"Título: {livro['titulo']}, Média: {livro['media_avaliacoes']:.2f}, Avaliações: {livro['total_avaliacoes']}")
        else:
            print("Nenhum livro com avaliações foi encontrado.")


