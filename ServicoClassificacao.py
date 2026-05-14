from Noticia import Noticia

# Classe responsável apenas pela lógica de classificação


class ServicoClassificacao:

    @staticmethod
    def classificar_texto_manualmente(texto, classificacao):
        noticia = Noticia(texto, classificacao)
        return noticia

    @staticmethod
    def classificar_texto_automaticamente(texto):
        noticia = Noticia(texto)
        noticia.analisar_qualidade()
        return noticia
