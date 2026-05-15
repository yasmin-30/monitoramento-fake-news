class Noticia:
    """
    Classe responsável pela representação de uma notícia.

    Armazena o texto da notícia, sua classificação e
    disponibiliza métodos para análise automática da
    qualidade da informação.
    """

    def __init__(self, texto, classificacao="pendente"):
        """
        Inicializa uma nova notícia.

        Args:
            texto (str): Conteúdo textual da notícia.
            classificacao (str, opcional): Classificação inicial
                da notícia. O valor padrão é "pendente".
        """

        self.texto = texto
        self.classificacao = classificacao

    def analisar_qualidade(self):  
        """
        Realiza a análise automática da qualidade da notícia.

        A classificação é definida com base em critérios simples,
        como uso de linguagem sensacionalista e tamanho reduzido
        do texto.

        Regras analisadas:
            - Presença de "!!!";
            - Presença da palavra "URGENTE";
            - Texto com menos de 10 caracteres.

        A classificação final pode ser:
            - confiavel;
            - duvidosa;
            - falsa.
        """


        confiabilidade = 0

        if "!!!" in self.texto:
            confiabilidade += 1

        if "URGENTE" in self.texto.upper():
            confiabilidade += 1

        if len(self.texto) < 10:
            confiabilidade += 1

        if confiabilidade == 0:
            self.classificacao = "confiavel"

        elif confiabilidade == 1:
            self.classificacao = "duvidosa"

        else:
            self.classificacao = "falsa"
