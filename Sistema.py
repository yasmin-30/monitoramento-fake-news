# sistema de noticias

noticias_avaliadas = []


# função que faz tudo
def persistir_textos_classificados(texto, classificacao=None):
    # essa função adiciona uma coisa
    if texto != "":
        texto_classificado = {}
        texto_classificado["texto"] = texto
        if classificacao == None:
            texto_classificado["classificacao"] = "duvidosa"
        else:
            texto_classificado["classificacao"] = classificacao
        noticias_avaliadas.append(texto_classificado)
    else:
        print("erro")


def listar_noticias_avaliadas():
    # lista tudo
    for i in range(0, len(noticias_avaliadas)):
        print("Texto:", noticias_avaliadas[i]["texto"])
        print("Classificacao:", noticias_avaliadas[i]["classificacao"])
        print("-------------------")


def analisar_texto_informado(texto):
    # analisa o texto
    confiabilidade = 0

    if "!!!" in texto:
        confiabilidade = confiabilidade + 1
    if "URGENTE" in texto:
        confiabilidade = confiabilidade + 1
    if len(texto) < 10:
        confiabilidade = confiabilidade + 1

    if confiabilidade == 0:
        return "confiavel"
    elif confiabilidade == 1:
        return "duvidosa"
    else:
        return "falsa"


def classificar_texto_manualmente():
    texto = input("Digite o texto: ")
    classificacao = input("Digite classificacao: ")

    if classificacao == "":
        persistir_textos_classificados(texto)
    else:
        persistir_textos_classificados(texto, classificacao)


def classificar_texto_automaticamente():
    texto = input("Digite o texto: ")
    classificacao = analisar_texto_informado(texto)
    persistir_textos_classificados(texto, classificacao)


def menu():
    while True:
        print("1 - adicionar manual")
        print("2 - adicionar automatico")
        print("3 - listar")
        print("4 - sair")

        opcao_selecionada = input("opcao: ")

        if opcao_selecionada == "1":
            classificar_texto_manualmente()
        elif opcao_selecionada == "2":
            classificar_texto_automaticamente()
        elif opcao_selecionada == "3":
            listar_noticias_avaliadas()
        elif opcao_selecionada == "4":
            break
        else:
            print("errado")


# comentarios desnecessarios abaixo
# inicia o programa
# chama o menu
menu()
