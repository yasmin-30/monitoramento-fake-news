from Modelo.Noticia import Noticia

class ServicoClassificacao:
    """
    Classe responsável pela lógica de classificação das notícias.

    Disponibiliza métodos para criação de notícias classificadas
    manualmente ou automaticamente com base nos critérios
    definidos pelo sistema.
    """

    @staticmethod
    def classificar_texto_manualmente(texto, classificacao):
        """
        Cria uma notícia com classificação definida manualmente.

        Args:
            texto (str): Conteúdo textual da notícia.
            classificacao (str): Classificação informada pelo usuário.

        Returns:
            Noticia: Objeto notícia contendo o texto e a
            classificação manual definida.
        """

        noticia = Noticia(texto, classificacao)
        return noticia

    @staticmethod
    def classificar_texto_automaticamente(texto):
        """
        Cria uma notícia e realiza sua classificação automática.

        A classificação é definida por meio da análise de
        qualidade implementada na classe Noticia.

        Args:
            texto (str): Conteúdo textual da notícia.

        Returns:
            Noticia: Objeto notícia classificado automaticamente.
        """

        noticia = Noticia(texto)
        noticia.analisar_qualidade()
        return noticia
