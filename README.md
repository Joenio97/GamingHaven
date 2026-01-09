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

super( ).__init__( atribtutos Jogos)

metodos:

**Class Coleção:**

atributos ( nome )

metodos: CriarColecao, adicionar, remover, editar, evitarDuplicação, listar

**Class Status:**

atributos: nãoIniciado, Jogando, finalizado

**Class Relatorio(Status)**

Self( ).__init__(atributos Status)

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

