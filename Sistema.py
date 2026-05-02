# sistema de noticias
# subbstituindo a lista global de textos classificados por uma classe que
# representa as propriedades de cada uma dessas notícias

# criei a classe notícia para substituir a lista global de notícias/textos que tinha antes.
# Com isso, a gente evita ter inconsistêscia e garante um formato único a cada uma das mensagens
# Além de poder classificar o conteúdo do objt na própria classe


class Noticia:

    # Troquei o 'None' provisóriamente por "pendente"
    def __init__(self, texto, classificacao="Pendente"):
        self.texto = texto
        self.classificacao = classificacao

    # coloquei o método de análise de qualidade como uma função intrínseca a cada objt notícia
    def analisar_qualidade(self):  # renomeação de função

        confiabilidade = 0

        if "!!!" in self.texto:
            confiabilidade += 1

        if "URGENTE" in self.texto:
            confiabilidade += 1

        if len(self.texto) < 10:
            confiabilidade += 1

        if confiabilidade == 0:
            self.classificacao = "Confiavel"
        # coloquei aqui parte da validação de dados que ficava na função 'faz tudo'
        elif (confiabilidade == 1) or (self.classificacao == "Pendente"):
            self.classificacao = "Duvidosa"
        else:
            self.classificacao = "Falsa"


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


# classes com funções específicas para o monitoramento das notícias/textos avaliado(a)s
class GerenciadorNoticias:

    def __init__(self):
        self._noticias = []  # Coloquei a lista de noticias como um atributo privado da classe

    # função que apenas armazena novos textos classificados na lista de noticias já avaliadas
    def persistir_textos_classificados(self, noticia: Noticia):
        self._noticias.append(noticia)

    def listar_noticias_avaliadas(self):
        # lista tudo
        for i in range(0, len(self._noticias)):
            print("Texto:", self._noticias[i].texto)
            print("Classificacao:", self._noticias[i].classificacao)
            print("-------------------")
        print(" ")


# função principal para interação com o usuário
def menu():

    gerenciador = GerenciadorNoticias()

    while True:
        print("1 - adicionar classificação de forma manual")
        print("2 - adicionar classificaçao de forma automática")
        print("3 - listar noticias classificadas")
        print("4 - sair")

        opcao_selecionada = input("opcao: ")

        if opcao_selecionada == "1":
            texto = input("Digite o texto: ")
            classificacao = input("Digite a classificacao: ")

            gerenciador.persistir_textos_classificados(
                ServicoClassificacao.classificar_texto_manualmente(texto, classificacao))

        elif opcao_selecionada == "2":
            texto = input("Digite o texto: ")
            gerenciador.persistir_textos_classificados(
                ServicoClassificacao.classificar_texto_automaticamente(texto))

        elif opcao_selecionada == "3":
            gerenciador.listar_noticias_avaliadas()

        elif opcao_selecionada == "4":
            break
        else:
            # nesse loop tem q verificar a validade do dado de opção também
            print("Opção Inválida. Tente novamente")


# comentarios desnecessarios abaixo
# inicia o programa
# chama o menu
menu()
