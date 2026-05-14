# criei a classe notícia para substituir a lista global de notícias/textos que tinha antes.
# Com isso, a gente evita ter inconsistêscia e garante um formato único a cada uma das mensagens
# Além de poder classificar o conteúdo do objt na própria classe


class Noticia:

    # Troquei o 'None' provisóriamente por "pendente"
    def __init__(self, texto, classificacao="pendente"):
        self.texto = texto
        self.classificacao = classificacao

    # coloquei o método de análise de qualidade como uma função intrínseca a cada objt notícia
    def analisar_qualidade(self):  # renomeação de função

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
