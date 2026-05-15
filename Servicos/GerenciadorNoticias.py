from Modelo.Noticia import Noticia

class GerenciadorNoticias:
    """
    Classe responsável pelo gerenciamento das notícias classificadas.

    Armazena as notícias avaliadas pelo sistema e disponibiliza
    funcionalidades para persistência e listagem das informações.
    """

    def __init__(self):
        """
        Inicializa o gerenciador com uma lista vazia de notícias.
        """

        self._noticias = [] 

    def persistir_textos_classificados(self, noticia: Noticia):
        """
        Armazena uma notícia classificada na lista de notícias avaliadas.

        Args:
            noticia (Noticia): Objeto do tipo Noticia que será armazenado.
        """

        self._noticias.append(noticia)

    def listar_noticias_avaliadas(self):
        """
        Exibe todas as notícias classificadas armazenadas no sistema.

        Caso não existam notícias cadastradas, o sistema informa
        ao usuário que ainda não há registros disponíveis.
        """

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
