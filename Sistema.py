# sistema de noticias
# subbstituindo a lista global de textos classificados por uma classe que
# representa as propriedades de cada uma dessas notícias

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
        print("\n--- LISTA DE NOTÍCIAS AVALIADAS ---")

        if self._noticias:
            # lista tudo
            for i in range(0, len(self._noticias)):
                print("\nTexto:", self._noticias[i].texto)
                print("Classificacao:", self._noticias[i].classificacao)
                print("-------------------")
            print(" ")
        
        else:
            print("\nAinda não há notícias classificadas.\nInsira notícias e tente novamente!\n")

class ValidacaoParametros:

    @staticmethod
    def validar_texto(texto):
        texto_valido = texto.strip()
        
        if texto_valido:
            return True

        return False

    @staticmethod
    def validar_classificacao(classificacao):        
        if classificacao in ['confiavel', 'duvidosa', 'falsa', 'pendente']:
            return True

        return False
    
    @staticmethod
    def validar_classificacao_correta(texto, classificacao_manual):
        noticia_teste = Noticia(texto)
        noticia_teste.analisar_qualidade()

        if noticia_teste.classificacao == classificacao_manual:
            return True
        
        return False

# função principal para interação com o usuário
def menu():

    gerenciador = GerenciadorNoticias()
    verificador = ValidacaoParametros()

    print("--- SISTEMA DE NOTÍCIAS ---\n")

    while True:
        print("1 - adicionar classificação de forma manual")
        print("2 - adicionar classificaçao de forma automática")
        print("3 - listar noticias classificadas")
        print("4 - sair")

        opcao_selecionada = input("opcao: ").strip()

        if opcao_selecionada == "1":
            texto = input("Digite o texto: ")
            classificacao = input("Digite a classificacao: ").strip().lower()

            texto_valido = verificador.validar_texto(texto)
            if not texto_valido:
                print("\nERRO: O texto inserido está vazio. Tente novamente!\n")
                continue
            
            classificacao_valida = verificador.validar_classificacao(classificacao)
            if not classificacao_valida:
                    print("\nERRO: A classificação inserida é inválida. Tente novamente!\n")
                    continue
            
            classificacao_correta = verificador.validar_classificacao_correta(texto, classificacao)
            if not classificacao_correta:
                print(f"\nALERTA: A classificação manual, {classificacao}, difere da análise automática do sistema!")
                confirmar = input("Deseja manter sua classificação assim mesmo? (s/n): ").strip().lower()

                if confirmar != 's':
                    print("Operação cancelada.\n")
                    continue
        
            gerenciador.persistir_textos_classificados(
                ServicoClassificacao.classificar_texto_manualmente(texto, classificacao))                

        elif opcao_selecionada == "2":
            texto = input("Digite o texto: ")
            texto_valido = verificador.validar_texto(texto)
            
            if not texto_valido:
                print("\nERRO: O texto inserido está vazio. Tente novamente!\n")
                continue
            
            gerenciador.persistir_textos_classificados(
                ServicoClassificacao.classificar_texto_automaticamente(texto))

        elif opcao_selecionada == "3":
            gerenciador.listar_noticias_avaliadas()

        elif opcao_selecionada == "4":
            print("\nEncerrando o sistema...")
            break

        else:
            # nesse loop tem q verificar a validade do dado de opção também
            print("\nERRO: Opção Inválida. Tente novamente!\n")


# comentarios desnecessarios abaixo
# inicia o programa
# chama o menu
menu()