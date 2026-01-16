# Projeto_POO

## Catalogo de Jogos Digitais

### Entrega 1

#### Integrantes de equipe e distribuição de tarefas

Joenio Borges de Araújo: Modelagem OO, classes Jogo e Status.

Maria Fernanda Sousa Silva: Regras de negócio, estados e classe coleção.

Matheus Moraes Bernardo: Persistência de dados e classe relatorios.

Kauê Oliveira Fernandes: Interface (CLI), classe progresso, testes e documentação.

Principais classes do projeto

**Class: Jogo**

atributos: titulo, genero, avaliação

metodos: cadastrar, gerenciar

**Class  JogoPc(Jogo):**

super( ).__init__( atributos Jogos)

**Class JogoMobile(jogo)**

super( ).__init__( atributos Jogos)

**Class JogoConsole(Jogo)

super( ).__init__( atributos Jogos)

metodos:

**Class Coleção:**

atributos ( nome )

metodos: CriarColecao, adicionar, remover, editar, evitarDuplicação, listar

**Class Relatorio**

atributos: tempoJogado

metodos: calcularMédia de avaliação dos jogos finalizados, 
calcularPercentual de jogos por status, listarTop 5 jogos mais jogados,
registrarInicio, registraTermino

**Class Progresso( Relatorio):**

super( ).__init__( atributos relatorio)

metodos: atualizarTempojogado, atualizarStatus

**Class filtros:**

metodos: FiltrarGênero, FiltrarPlataforma, FiltrarStatus, FiltrarTitulo, BuscarParte doTitulo.


# Entrega 2 

Nessa etapa, foi desenvolvida a implementação inicial do sistema de catálogo de jogos digitais.
 
  * Implementação da classe base Jogo com atributos e regras principais.

  * Aplicação de encapsulamento, utilizando @property para validar as horas jogadas e avaliação.
    
  * Aplicação de regras de negócio para progresso e finalização de jogos.
    
  * Implementação de herança nas classes JogoPC, JogoConsole e JogoMobile.

  * Definição de regras de negócio, impedindo valores inválidos e ações inconsistentes no sistema.

  * Implementação de herança nas classes JogoPC, JogoConsole e JogoMobile.

  * Criação do arquivo main.py para demonstrar o funcionamento do sistema.
  
  * Implementação de métodos especiais (__str__, __repr__, __eq__, __lt__) para representação, comparação e ordenação de objetos.

  * Organização do código em módulos visando fácil evolução do projeto.

## Entrega 3

### 🎮 GamingHaven - Catálogo de Jogos
Aplicação CLI (Command Line Interface) para gerenciamento e persistência de uma biblioteca de jogos pessoal.

📋 Instruções de Uso
Pré-requisitos:

Python 3.10 ou superior.

Poetry instalado.

**Instalação:**

1.Clone o repositório.

2.No terminal, dentro da pasta do projeto, instale as dependências, digite o seguinte comando e aperte ENTER:


poetry install

**Executando a aplicação:**

Para iniciar o menu principal, utilize o comando:

poetry run catalogo

### Arquitetura e Design

O projeto utiliza os princípios da Programação Orientada a Objetos (POO) e uma estrutura de pastas organizada para separar as responsabilidades.

Decisões de Design:

* Herança: Utilizamos uma classe base Jogo que contém atributos comuns (título, gênero, plataforma). Classes específicas como jogoPC, jogoMobile e jogoConsole herdam de Jogo, permitindo comportamentos específicos e evitando repetição de código.

* Separação de Camadas: * dominio: Contém as regras de negócio e definições de objetos.

* dados: Responsável pela persistência (neste caso, leitura e escrita em arquivos JSON).

* cli.py: Gerencia a interação com o usuário.

* Persistência: Optamos por JSON para o armazenamento de dados por ser um formato leve, legível por humanos e nativamente suportado pelo Python, facilitando a portabilidade do catálogo.

* Gestão de Dependências: O Poetry foi escolhido para garantir que o ambiente virtual e as bibliotecas sejam consistentes em qualquer máquina.


