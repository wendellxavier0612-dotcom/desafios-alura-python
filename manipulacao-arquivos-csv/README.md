# Controle de Notas - Escola PythonVille

Exercício da trilha Python do Alura. O programa registra alunos e suas notas
em um arquivo CSV e permite consultar quem teve nota igual ou maior que 7.0.

## O que o programa faz

1. Menu interativo com 3 opções: registrar aluno, visualizar aprovados, encerrar.
2. Ao registrar, grava o nome e a nota no arquivo `alunos.csv` (todos os alunos,
   aprovados ou não).
3. Ao visualizar, lê o `alunos.csv` inteiro e imprime apenas os alunos com
   nota >= 7.0 — o filtro acontece na leitura, não na escrita.

## Como rodar

```bash
python controle_notas.py
```

## O que pratiquei

- Leitura e escrita de arquivos CSV com o módulo `csv` (`csv.writer` / `csv.reader`)
- Diferença entre os modos de abertura de arquivo (`'r'`, `'w'`, `'a'`) e o
  motivo de cada um se comportar diferente com dados já existentes
- Tratamento de exceções (`try/except`) para entradas inválidas do usuário e
  para arquivos que ainda não existem
- Controle de fluxo de menu com `while True`, `continue` e `break`, evitando
  recursão desnecessária

## Principais erros que cometi e corrigi

Errar faz parte do processo, e documentar isso aqui é mais útil do que
esconder — foi o que mais me ajudou a fixar os conceitos:

- **Escrevia com `open(..., 'w')`** ao registrar cada aluno, o que apagava o
  arquivo inteiro a cada novo cadastro. Troquei para `'a'` (append), que
  acrescenta sem sobrescrever o que já existia.
- **Esquecia o `newline=''`** ao abrir o CSV, o que fazia o Windows gravar uma
  quebra de linha extra — na leitura, isso virava uma linha vazia e quebrava o
  programa com `IndexError`.
- **Usava recursão (chamando `menu()` dentro do próprio `menu()`)** para voltar
  ao início do fluxo, em vez de deixar o `while True` já existente cuidar
  disso. Isso empilhava várias execuções da função ao mesmo tempo sem
  necessidade. Troquei por `continue`/`break`, que controlam o loop sem criar
  chamadas novas.
- **Comparava a nota lida do CSV diretamente com um número**, sem lembrar que
  tudo que vem de um arquivo de texto chega como `str` — precisei converter
  com `float()` antes de comparar com `>= 7`.
- **Não tratava o caso de visualizar antes de qualquer aluno estar
  cadastrado**, o que gerava `FileNotFoundError`. Adicionei um `try/except`
  para esse cenário.
