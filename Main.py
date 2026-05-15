# sistema de noticias
# subbstituindo a lista global de textos classificados por uma classe que
# representa as propriedades de cada uma dessas notícias

# criei a classe notícia para substituir a lista global de notícias/textos que tinha antes.
# Com isso, a gente evita ter inconsistêscia e garante um formato único a cada uma das mensagens
# Além de poder classificar o conteúdo do objt na própria classe


from Serviços.GerenciadorNoticias import GerenciadorNoticias
from Utilitarios.ValidacaoParametros import ValidacaoParametros
from Interface.MenuNoticias import MenuNoticias

if __name__ == "__main__":
    # Configuração do Sistema
    gerenciador = GerenciadorNoticias()
    verificador = ValidacaoParametros()

    # Inicia a Interface
    sistema = MenuNoticias(gerenciador, verificador)
    sistema.menu()
