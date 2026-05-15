"""
Sistema de Monitoramento de Fake News e Qualidade da Informação.

Este módulo é responsável pela inicialização do sistema,
realizando a configuração dos componentes principais e
executando a interface textual da aplicação.
"""

from Servicos.GerenciadorNoticias import GerenciadorNoticias
from Utilitarios.ValidacaoParametros import ValidacaoParametros
from Interface.MenuNoticias import MenuNoticias

if __name__ == "__main__":
    """
    Ponto de entrada principal da aplicação.

    Realiza a configuração inicial do sistema, instanciando
    os componentes responsáveis pelo gerenciamento das notícias,
    validação de dados e interface com o usuário.
    """

    # Configuração do Sistema
    gerenciador = GerenciadorNoticias()
    verificador = ValidacaoParametros()

    # Inicializa a interface principal do sistema
    sistema = MenuNoticias(gerenciador, verificador)

    # Inicia a execução do menu interativo
    sistema.menu()
