from ServicoClassificacao import ServicoClassificacao


class ValidacaoParametros:

    @staticmethod
    def validar_texto(texto):
        texto_valido = texto.strip()

        if texto_valido:
            return True

        return False

    @staticmethod
    def validar_classificacao(classificacao):
        if classificacao in ['confiavel', 'duvidosa', 'falsa']:
            return True

        return False

    @staticmethod
    def validar_classificacao_correta(texto, classificacao_manual):
        noticia_sistema = ServicoClassificacao.classificar_texto_automaticamente(
            texto)

        if noticia_sistema.classificacao == classificacao_manual:
            return True, classificacao_manual

        return False, noticia_sistema.classificacao
