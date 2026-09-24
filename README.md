# 🐍 Jornada Python — Aula 01

Projeto desenvolvido durante a **Jornada Python**, evento promovido pela **Hashtag Treinamentos**, como parte dos meus estudos de programação.

Esta é a primeira aula do evento e foi realizada em **2024**, tendo como foco a criação de uma **automação de tarefas utilizando Python e PyAutoGUI**.

---

## 📚 Sobre a aula

Nesta aula, o objetivo foi aprender como utilizar o Python para **automatizar tarefas repetitivas**, simulando ações que normalmente seriam realizadas manualmente no computador.

O projeto utiliza uma base de dados com informações de produtos e automatiza o processo de cadastro dessas informações em um sistema.

A automação realiza etapas como:

- Abrir o navegador;
- Acessar o sistema;
- Realizar o login;
- Percorrer a base de dados;
- Preencher os campos dos produtos;
- Enviar os cadastros;
- Repetir o processo até finalizar todos os produtos.

A proposta é demonstrar como tarefas repetitivas podem ser automatizadas para **economizar tempo e reduzir erros de preenchimento**.

---

## 🗂️ Base de dados

Os dados utilizados no projeto estão armazenados no arquivo:

`produtos.csv`

A base contém informações como:

- Código do produto;
- Marca;
- Tipo;
- Preço unitário;
- Custo;
- Observação.

A aula utiliza a biblioteca **pandas** para importar e visualizar essa base de dados antes de iniciar a automação.

---

## 🤖 Automação com PyAutoGUI

A principal biblioteca utilizada no projeto é a **PyAutoGUI**, responsável por permitir que o Python controle o **mouse e o teclado**.

Entre os comandos utilizados na aula estão:

- `pyautogui.press()` — pressiona uma tecla do teclado;
- `pyautogui.write()` — escreve utilizando o teclado;
- `pyautogui.click()` — realiza um clique do mouse;
- `pyautogui.scroll()` — movimenta o scroll do mouse;
- `pyautogui.PAUSE` — define um intervalo entre os comandos.

Também foi utilizado um código auxiliar para obter a **posição do mouse**, já que as coordenadas utilizadas pelo `pyautogui.click()` são baseadas na posição do elemento na tela.

> ⚠️ As coordenadas do mouse podem variar de acordo com o monitor e a resolução utilizada. Por isso, é necessário obter as posições no próprio computador antes de executar a automação.

---

## 🔄 Lógica da automação

Depois de abrir o navegador e realizar o login, o programa utiliza uma estrutura de repetição `for` para percorrer as linhas da base de dados.

Para cada produto, o programa:

1. Localiza as informações correspondentes na tabela;
2. Preenche os campos do sistema;
3. Verifica se existe alguma observação;
4. Envia o cadastro;
5. Passa para o próximo produto.

Dessa forma, o mesmo processo é repetido automaticamente até que todos os produtos sejam cadastrados.

---

## 🛠️ Tecnologias e conceitos utilizados

### Linguagem

- Python

### Bibliotecas

- Pandas
- PyAutoGUI

### Conceitos praticados

- Importação de bibliotecas
- Leitura de arquivos `.csv`
- Manipulação de dados com Pandas
- Estrutura de repetição `for`
- Estrutura condicional `if`
- Manipulação do DOM da tela através de ações do mouse e teclado
- Eventos de teclado
- Cliques através de coordenadas
- Controle de tempo com `time.sleep()`
- Automação de tarefas repetitivas

---

## 📸 Fotos e vídeos do projeto

Esta seção é destinada aos registros da execução do programa.

### 🖥️ Execução do programa

[▶️ Assistir ao vídeo da automação](./assets/0923.mp4)

---

## 📖 O que aprendi

A aula me permitiu conhecer uma aplicação prática do **Python para automação de tarefas**, mostrando como uma sequência de ações realizadas manualmente pode ser transformada em um processo automatizado.

Também pratiquei a leitura de dados utilizando **Pandas** e a utilização do **PyAutoGUI** para controlar o computador através de comandos de Python.

---

## 🎓 Sobre a Jornada Python

Este projeto faz parte da **Jornada Python**, evento promovido pela **Hashtag Treinamentos**.

📅 **Ano:** 2024  
⏱️ **Carga horária do evento:** 8 horas  
📅 **Conclusão:** 10 de outubro de 2024  
🐍 **Tema:** Python

Este repositório corresponde **somente à primeira aula** do evento.

---

## 🔗 Referência

Material de estudo utilizado durante a aula:

**Jornada Python — Hashtag Treinamentos**

A apostila da aula aborda a construção de uma automação para cadastro de produtos utilizando Python, Pandas e PyAutoGUI.

---

## 👩‍💻 Autora

**Lua**

Estudante de **Sistemas para Internet**, com interesse em desenvolvimento web, programação e tecnologia.

---

<p align="center">
  Projeto desenvolvido durante meus estudos de Python. 🐍💻
</p>
