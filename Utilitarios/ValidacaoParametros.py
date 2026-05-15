from Servicos.ServicoClassificacao import ServicoClassificacao


class ValidacaoParametros:
    """
    Classe responsável pelas validações do sistema.

    Realiza verificações relacionadas às entradas do usuário,
    garantindo maior integridade e confiabilidade dos dados
    processados pela aplicação.
    """

    @staticmethod
    def validar_texto(texto):
        """
        Verifica se o texto informado é válido.

        Remove espaços em branco das extremidades e impede
        o cadastro de textos vazios.

        Args:
            texto (str): Texto inserido pelo usuário.

        Returns:
            bool: True caso o texto seja válido.
            False caso o texto esteja vazio.
        """

        texto_valido = texto.strip()

        if texto_valido:
            return True

        return False

    @staticmethod
    def validar_classificacao(classificacao):
        """
        Verifica se a classificação informada pertence
        às categorias permitidas pelo sistema.

        Classificações válidas:
            - confiavel
            - duvidosa
            - falsa

        Args:
            classificacao (str): Classificação inserida pelo usuário.

        Returns:
            bool: True caso a classificação seja válida.
            False caso seja inválida.
        """

        if classificacao in ['confiavel', 'duvidosa', 'falsa']:
            return True

        return False

    @staticmethod
    def validar_classificacao_correta(texto, classificacao_manual):
        """
        Compara a classificação manual informada pelo usuário
        com a classificação automática sugerida pelo sistema.

        Args:
            texto (str): Conteúdo textual da notícia.
            classificacao_manual (str): Classificação definida manualmente.

        Returns:
            tuple:
                - True e a classificação manual, caso exista compatibilidade;
                - False e a classificação sugerida pelo sistema,
                  caso exista divergência.
        """

        noticia_sistema = ServicoClassificacao.classificar_texto_automaticamente(
            texto)

        if noticia_sistema.classificacao == classificacao_manual:
            return True, classificacao_manual

        return False, noticia_sistema.classificacao
