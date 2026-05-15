from Servicos.ServicoClassificacao import ServicoClassificacao


class MenuNoticias:
    """
    Classe responsável pela interface textual do sistema.

    Controla a interação com o usuário, captura entradas,
    realiza validações e coordena o fluxo principal da aplicação.
    """

    def __init__(self, gerenciador, verificador):
        """
        Inicializa o menu do sistema.

        Args:
            gerenciador: Instância responsável pelo gerenciamento
                das notícias classificadas.
            verificador: Instância responsável pelas validações
                de entradas do sistema.
        """

        self.gerenciador = gerenciador
        self.verificador = verificador

    def obter_texto(self):
        """
        Solicita ao usuário o texto da notícia e valida a entrada.

        Returns:
            str | None: Retorna o texto inserido caso seja válido.
            Caso contrário, retorna None.
        """

        texto = input("\nDigite o texto: ")
        texto_valido = self.verificador.validar_texto(texto)

        if texto_valido:
            return texto

        return None

    def obter_classificacao(self):
        """
        Solicita ao usuário uma classificação manual para a notícia.

        Returns:
            str | None: Retorna a classificação válida informada
            pelo usuário. Caso a entrada seja inválida, retorna None.
        """

        print("Opções: confiavel, duvidosa, falsa")
        classificacao = input("Digite a classificação: ").strip().lower()
        classificacao_valida = self.verificador.validar_classificacao(
            classificacao)

        if classificacao_valida:
            return classificacao

        return None

    def resolver_conflito(self, texto, classificacao_manual):
        """
        Verifica inconsistências entre a classificação manual
        e a classificação sugerida pelo sistema.

        Caso exista divergência, o usuário pode decidir
        entre manter a classificação manual ou utilizar
        a classificação automática.

        Args:
            texto (str): Texto da notícia analisada.
            classificacao_manual (str): Classificação inserida pelo usuário.

        Returns:
            str: Classificação final escolhida.
        """

        classificacao_correta, classificacao_sistema = self.verificador.validar_classificacao_correta(
            texto, classificacao_manual)

        if classificacao_correta:
            return classificacao_manual

        else:
            print(
                f"\nALERTA: O sistema sugere '{classificacao_sistema}', mas você digitou '{classificacao_manual}'.")

            while True:
                escolha_classificacao = input(
                    "Deseja manter a classificação inserida? (s/n)").strip().lower()

                if escolha_classificacao == 's':
                    return classificacao_manual

                elif escolha_classificacao == 'n':
                    return classificacao_sistema

                print("ERRO: Opção inválida")

    def menu(self):
        """
        Executa o menu principal do sistema.

        Permite ao usuário adicionar notícias manualmente
        ou automaticamente, listar notícias classificadas
        e encerrar o sistema.
        """


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
                        print(
                            "\nERRO: A classificação inserida é inválida. Tente novamente!\n")
                        continue

                    classificacao_correta = self.resolver_conflito(
                        texto_valido, classificacao_valida)
                    if not classificacao_correta:
                        continue

                    noticia_classificada = ServicoClassificacao.classificar_texto_manualmente(
                        texto_valido, classificacao_correta)

                else:
                    noticia_classificada = ServicoClassificacao.classificar_texto_automaticamente(
                        texto_valido)

                self.gerenciador.persistir_textos_classificados(
                    noticia_classificada)

            elif opcao_selecionada == "3":
                self.gerenciador.listar_noticias_avaliadas()

            elif opcao_selecionada == "4":
                print("\nEncerrando o sistema...")
                break

            else:
                # nesse loop tem q verificar a validade do dado de opção também
                print("\nERRO: Opção Inválida. Tente novamente!\n")
