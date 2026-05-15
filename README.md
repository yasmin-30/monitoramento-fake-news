# Sistema de Monitoramento de Fake News e Qualidade da Informação

## Objetivo do Sistema

O sistema foi desenvolvido para cadastrar, analisar e classificar notícias de acordo com sua confiabilidade. O objetivo principal é auxiliar na identificação de possíveis fake news por meio de critérios básicos de análise textual.

---

## Funcionalidades Disponíveis

* Cadastro manual de notícias;
* Classificação automática de notícias;
* Validação de entradas do usuário;
* Listagem das notícias classificadas;
* Verificação de inconsistências entre classificação manual e automática;
* Tratamento de erros e mensagens informativas ao usuário.

---

## Estrutura do Projeto

### Hierarquia de Arquivos

projeto/
├── Interface/
│   └── MenuNoticias.py
├── Modelo/
│   └── Noticia.py
├── Servicos/
│   ├── GerenciadorNoticias.py
│   └── ServicoClassificacao.py
├── Utilitarios/
│   └── ValidacaoParametros.py
├── Main.py
└── README.md

## Organização de Camadas

### Interface
Contém os módulos responsáveis pela interação com o usuário.

### Modelo
Define as entidades e estruturas fundamentais do sistema.

### Servicos
Concentra a lógica de negócio, processamento de dados e classificações.

### Utilitarios
Reúne funções auxiliares voltadas à sanitização e validação de parâmetros.

---

## Estrutura dos Módulos e Classes

### Noticia.py

Responsável pela representação das notícias e pela análise automática da qualidade da informação.

### ServicoClassificacao.py

Responsável pela lógica de classificação manual e automática das notícias.

### GerenciadorNoticias.py

Responsável pelo armazenamento e listagem das notícias classificadas.

### ValidacaoParametros.py

Responsável pelas validações de textos e classificações inseridas no sistema.

### MenuNoticias.py

Responsável pela interface textual e interação com o usuário.

### Sistema.py

Arquivo principal responsável pela inicialização e execução do sistema.

---

## Lógica de Classificação das Notícias

A classificação automática é realizada com base nos seguintes critérios:

* Uso de linguagem sensacionalista, como “URGENTE”;
* Presença de múltiplos sinais de exclamação (“!!!”);
* Textos muito curtos.

De acordo com a quantidade de critérios identificados, a notícia pode ser classificada como:

* confiavel;
* duvidosa;
* falsa.

---

## Instruções de Execução do Programa

1. Certifique-se de possuir o Python instalado na máquina;
2. Mantenha todos os arquivos do projeto na mesma pasta;
3. Execute o arquivo Main.py;
4. Utilize o menu exibido no terminal para interagir com o sistema.

---

## Melhorias Aplicadas Durante a Manutenção

* Refatoração de funções e variáveis com nomes genéricos;
* Separação das responsabilidades em classes e módulos;
* Implementação de programação orientada a objetos;
* Remoção de código duplicado;
* Adição de validações de entrada;
* Implementação de tratamento de erros mais descritivo;
* Organização estrutural do sistema para facilitar manutenção e expansão.

---

## Conceitos e Boas Práticas Utilizados

* Modularização;
* Programação Orientada a Objetos (POO);
* Responsabilidade Única (SRP);
* Programação Defensiva;
* Refatoração de código;
* DRY (Don’t Repeat Yourself);
* Encapsulamento;
* Nomenclatura descritiva;
* Organização e legibilidade de código.
