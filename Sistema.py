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
        if classificacao in ['confiavel', 'duvidosa', 'falsa']:
            return True

        return False
    
    @staticmethod
    def validar_classificacao_correta(texto, classificacao_manual):
        noticia_sistema = ServicoClassificacao.classificar_texto_automaticamente(texto)

        if noticia_sistema.classificacao == classificacao_manual:
            return True, classificacao_manual
        
        return False, noticia_sistema.classificacao


class MenuNoticias:
    
    def __init__(self, gerenciador, verificador):
        self.gerenciador = gerenciador
        self.verificador = verificador

    def obter_texto(self):
        texto = input("\nDigite o texto: ")
        texto_valido = self.verificador.validar_texto(texto)

        if texto_valido:
            return texto
        
        return None
    
    def obter_classificacao(self):
        print("Opções: confiavel, duvidosa, falsa")
        classificacao = input("Digite a classificação: ").strip().lower()
        classificacao_valida = self.verificador.validar_classificacao(classificacao)
    
        if classificacao_valida:
            return classificacao
        
        return None
    
    def resolver_conflito(self, texto, classificacao_manual):
        classificacao_correta, classificacao_sistema = self.verificador.validar_classificacao_correta(texto, classificacao_manual)
        
        if classificacao_correta:
            return classificacao_manual
        
        else:
            print(f"\nALERTA: O sistema sugere '{classificacao_sistema}', mas você digitou '{classificacao_manual}'.")
           
            while True:
                escolha_classificacao = input("Deseja manter a classificação inserida? (s/n)").strip().lower()
                
                if escolha_classificacao == 's':
                    return classificacao_manual
               
                elif escolha_classificacao == 'n':
                    return classificacao_sistema
               
                print("ERRO: Opção inválida")

    # função principal para interação com o usuário
    def menu(self):

        print("--- SISTEMA DE NOTÍCIAS ---\n")

        while True:
            print("1 - adicionar classificação de forma manual")
            print("2 - adicionar classificaçao de forma automática")
            print("3 - listar noticias classificadas")
            print("4 - sair")

            opcao_selecionada = input("opcao: ").strip()

            if opcao_selecionada in ["1", "2"]:
                texto_valido = self.obter_texto()
                if not texto_valido:
                    print("\nERRO: O texto inserido está vazio. Tente novamente!\n")
                    continue

                if opcao_selecionada == "1":    
                    classificacao_valida = self.obter_classificacao()
                    if not classificacao_valida:
                        print("\nERRO: A classificação inserida é inválida. Tente novamente!\n")
                        continue 

                    classificacao_correta = self.resolver_conflito(texto_valido, classificacao_valida) 
                    if not classificacao_correta:
                        continue  
                
                    noticia_classificada = ServicoClassificacao.classificar_texto_manualmente(texto_valido, classificacao_correta) 
                
                else:
                    noticia_classificada = ServicoClassificacao.classificar_texto_automaticamente(texto_valido)
                
                self.gerenciador.persistir_textos_classificados(noticia_classificada)

            elif opcao_selecionada == "3":
                self.gerenciador.listar_noticias_avaliadas()

            elif opcao_selecionada == "4":
                print("\nEncerrando o sistema...")
                break

            else:
                # nesse loop tem q verificar a validade do dado de opção também
                print("\nERRO: Opção Inválida. Tente novamente!\n")

if __name__ == "__main__":
    # Configuração do Sistema
    gerenciador = GerenciadorNoticias()
    verificador = ValidacaoParametros()
    
    # Inicia a Interface
    sistema = MenuNoticias(gerenciador, verificador)
    sistema.menu()