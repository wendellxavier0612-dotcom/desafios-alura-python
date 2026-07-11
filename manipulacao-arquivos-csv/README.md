# Manipulação de Arquivos CSV - Controle de Notas

Programa em Python que registra notas de alunos e consulta quem teve bom
desempenho, utilizando leitura e escrita de arquivos no formato CSV.

## 📋 Sobre o desafio

Na Escola PythonVille, o professor precisa registrar as notas dos alunos e
depois consultar quem teve nota igual ou maior que 7.0, mantendo esse
registro salvo para uso futuro. O programa foi construído com um menu
interativo via terminal, onde o usuário cadastra os alunos e consulta os
aprovados a qualquer momento.

## ⚙️ Funcionalidades

- Registrar aluno(a) com nome e nota, gravando os dados em `alunos.csv`
- Registrar múltiplos alunos em sequência sem precisar voltar ao menu manualmente
- Visualizar apenas os alunos com nota maior ou igual a 7.0
- Persistência dos dados entre execuções do programa

## 🧠 Conceitos praticados

- Leitura e escrita de arquivos com `open()` e o módulo `csv`
- Modos de abertura de arquivo (`'r'`, `'w'`, `'a'`) e o comportamento de cada um
- Tratamento de exceções com `try/except`
- Controle de fluxo com `while`, `continue` e `break`
- Conversão de tipos (`str` para `float`) na leitura de dados

## 🛠️ Tecnologias

- Python 3
- Módulo `csv`
- Módulo `os`

## ▶️ Como executar

```bash
python controle_notas.py
```

## 📚 Sobre

Exercício criado durante meus estudos de Python na [Alura](https://www.alura.com.br/),
como prática de manipulação de arquivos.