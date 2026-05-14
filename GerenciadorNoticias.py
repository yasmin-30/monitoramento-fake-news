from Noticia import Noticia

# classes com funções específicas para o monitoramento das notícias/textos avaliado(a)s


class GerenciadorNoticias:

    def __init__(self):
        self._noticias = []  # Coloquei a lista de noticias como um atributo privado da classe

    # função que apenas armazena novos textos classificados na lista de noticias já avaliadas
    def persistir_textos_classificados(self, noticia: Noticia):
        self._noticias.append(noticia)

    def listar_noticias_avaliadas(self):
        print("\n--- LISTA DE NOTÍCIAS AVALIADAS ---")

        if self._noticias:
            # lista tudo
            for i in range(0, len(self._noticias)):
                print("\nTexto:", self._noticias[i].texto)
                print("Classificacao:", self._noticias[i].classificacao)
                print("-------------------")
            print(" ")

        else:
            print(
                "\nAinda não há notícias classificadas.\nInsira notícias e tente novamente!\n")
