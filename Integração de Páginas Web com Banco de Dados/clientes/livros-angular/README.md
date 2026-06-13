# Catálogo de Livros em Angular - Manual do Projeto

Este projeto consiste em um sistema de catálogo de livros desenvolvido com o framework Angular. Ele tem como principal objetivo demonstrar a proficiência na utilização das ferramentas e bibliotecas do Angular para gerenciamento de dados de front-end.

## Objetivo do Trabalho

A atividade prática demandou o cumprimento dos seguintes requisitos técnicos:

1.  **Serviços Injetáveis**: Criação e implementação de serviços para gestão de estado no Angular através do TypeScript.
2.  **Componentes Angular**: Desenvolvimento de interfaces compostas por classes TypeScript e modelos HTML.
3.  **Gerenciamento de Formulários**: Utilização da biblioteca do Angular (`FormsModule` e `ngModel`) para criação e captura bidirecional de dados.
4.  **Sistema de Navegação Interna**: Implementação de roteamento front-end para transição entre as telas (listagem e cadastro) sem recarregamento da página.

## Estrutura do Projeto

Os arquivos fonte principais encontram-se em `src/app/` e estão estruturados da seguinte maneira:

*   **Modelos**:
    *   `livro.ts`: Define a estrutura dos livros (código, código da editora, título, resumo e autores).
    *   `editora.ts`: Define a estrutura da editora (código e nome).
*   **Serviços Injetáveis**:
    *   `controle-livros.service.ts`: Controlador para adicionar, listar e remover livros da memória.
    *   `controle-editora.service.ts`: Controlador que retorna a listagem estática de editoras do sistema e converte códigos no nome formatado da editora.
*   **Componentes**:
    *   **LivroListaComponent** (`livro-lista`): Consome os controladores para apresentar os livros cadastrados em formato de tabela. Relaciona códigos de editora a nomes e possibilita a exclusão de um registro existente.
    *   **LivroDadosComponent** (`livro-dados`): Disponibiliza o formulário para cadastro. Utiliza o método nativo de validações do HTML5 e os módulos do Angular para construir um novo objeto Livro a partir das entradas de texto e caixas de seleção, inserindo-o no controlador em memória antes de redirecionar à tela inicial.
*   **Módulo Base**:
    *   `app.module.ts`: Unifica componentes e serviços provendo o contexto para injeção de dependências e importando o `FormsModule`.
    *   `app-routing.module.ts`: Gerencia as rotas `/lista` e `/dados`.

## Como Executar

### Requisitos Prévios
*   Ambiente de desenvolvimento NodeJS instalado.
*   Navegador de internet atualizado.

### Passos
1.  Acesse o diretório raiz do projeto `livros-angular` via terminal.
2.  Execute o comando para instalar as dependências (caso seja a primeira execução):
    ```bash
    npm install
    ```
3.  Inicialize o servidor de desenvolvimento utilizando a CLI do Angular:
    ```bash
    ng serve
    ```
4.  Abra seu navegador e navegue para o endereço local padrão:
    ```
    http://localhost:4200/
    ```

A aplicação fará a recompilação automática caso qualquer um dos arquivos fonte seja modificado, mantendo a estabilidade e fluidez nos testes do sistema.
