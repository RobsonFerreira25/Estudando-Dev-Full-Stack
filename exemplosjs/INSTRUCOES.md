# Guia de Instruções e Testes - Trabalho de Javascript e DOM

Este diretório contém a resolução dos 3 procedimentos propostos para a atividade da faculdade. Abaixo está a explicação de cada arquivo e o guia rápido de como testar as funcionalidades implementadas.

## Como Executar o Projeto
Não é necessária nenhuma instalação especial. Você pode simplesmente abrir qualquer um dos arquivos `.html` diretamente no seu navegador de preferência (Google Chrome, Firefox, Edge, etc) dando um duplo-clique no arquivo.

Caso queira uma experiência melhor, utilize a extensão **Live Server** do VSCode ou um servidor web simples.

---

## 1º Procedimento: Ordenando com JavaScript e DOM
**Arquivo:** `ordenando.html` e `ordenando.js`

Este projeto permite criar uma lista de números dinâmica e aplicar métodos de ordenação.
- O arquivo `ordenando.js` contém a implementação de três algoritmos de ordenação em **Arrow Functions**: Bubble Sort, Selection Sort e Quick Sort (com a função auxiliar particionamento). Também possui a função Shuffle e Swap.
- O arquivo `ordenando.html` possui scripts Javascript Clássico para realizar a manipulação no DOM (adicionar, listar, substituir valores) baseando-se em `map` e `reduce`.

### Como Testar:
1. Abra o arquivo `ordenando.html` no navegador.
2. Digite um número e clique em **Adicionar** (adicione uns 5 números aleatórios).
3. Selecione o algoritmo desejado na caixa de opções.
4. Clique em **Ordenar** para verificar se os números foram ordenados de forma crescente.
5. Clique em **Misturar** para que as posições da lista fiquem embaralhadas de forma aleatória.

---

## 2º Procedimento: Página de Receitas Dinâmica
**Arquivo:** `receitas.html`
*(Imagens utilizadas: arroz_couve_flor.png, bolo_cafe.png, coxinha_brigadeiro.png)*

Este projeto consiste na criação de um catálogo estilizado em Bootstrap de forma dinâmica baseada em um array JSON.

### Como Testar:
1. Abra o arquivo `receitas.html` no navegador.
2. Verifique o layout (Painel laranja com design flex-wrap e cards de largura 250px).
3. Todo o conteúdo visível na tela (incluindo imagens geradas por Inteligência Artificial e a lista de ingredientes) não foi escrito diretamente no HTML. Eles são injetados na tela automaticamente usando `map` e `reduce` assim que o `onload` no body é acionado.

---

## 3º Procedimento: Transmissão de Dados e VUE JS
**Arquivo:** `usuarios.html` e `users.json`

Este projeto consome uma "API REST" assíncrona utilizando **Vue.js (v2)**, **Bootstrap** e a **Fetch API**.

*(Nota de adaptação: O site oficial da atividade `reqres.in` começou a cobrar "chaves de acesso" recentemente para fornecer os dados. Para evitar que o sistema quebrasse, baixamos a resposta JSON oficial do reqres para o arquivo local `users.json` contendo fotos originais e realistas para os usuários, mas a requisição assíncrona Fetch continua trabalhando perfeitamente com os dados e mantendo a lógica de nota do trabalho).*

### Como Testar:
1. Abra o arquivo `usuarios.html` no navegador.
2. Aguarde o evento `mounted` do Vue ser disparado.
3. Repare que três componentes dinâmicos (cards) foram construídos a partir de um looping reativo (`v-for`) listando a Foto (Avatar), o Nome/Sobrenome e o E-mail de cada pessoa.

---
