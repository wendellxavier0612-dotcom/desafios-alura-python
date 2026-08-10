# Strings e Regex

Exercícios práticos de **manipulação de strings** e **expressões regulares (regex)** em Python, parte do curso da [Alura](https://www.alura.com.br/).

## 📂 Exercícios

- **decifrar_pistas.py** — Extrai as três primeiras e três últimas letras de uma palavra usando slicing (`[:3]` e `[-3:]`)
- **formatando_uma_saudacao.py** — Monta uma saudação personalizada combinando nome e cidade em uma f-string
- **ajustando_nomes_dos_produtos.py** — Padroniza o nome de um produto deixando em minúsculo e removendo espaços extras (`.lower()`, `.strip()`)
- **start-endswith.py** — Valida se uma URL começa com `"https://"` e termina com `".com"`, usando `.startswith()` e `.endswith()`
- **busca_pela_primeira_letra.py** — Busca, em um texto, todas as palavras que começam com uma letra específica, usando regex (`re.findall`)
- **encontrando_numeros_em_um_texto.py** — Encontra o primeiro número presente em um texto usando `re.findall(r'\d+', ...)`
- **substituindo_palavras.py** — Substitui uma palavra por outra dentro de um texto, usando `re.sub` com limites de palavra (`\b`)
- **criando_nome_padronizado.py** — Valida se um nome segue o padrão "primeira letra maiúscula, restante minúsculo", usando `re.fullmatch`
- **verificando_formato_CPF.py** — Valida se um CPF está no formato `XXX.XXX.XXX-XX`, usando `re.fullmatch` com uma regex de dígitos
- **agrupar_informações.py** — Extrai nome, sobrenome e ano de nascimento de um texto usando grupos de captura em regex (`re.fullmatch` + `.group()`)

## 🧠 Conceitos praticados

- Fatiamento de strings (*slicing*) com índices positivos e negativos
- Métodos de string: `.lower()`, `.strip()`, `.startswith()`, `.endswith()`
- Expressões regulares com o módulo `re`: `re.findall`, `re.sub`, `re.fullmatch`
- Construção de padrões regex: classes de caracteres, quantificadores (`+`, `{n}`), grupos de captura `(...)` e limites de palavra (`\b`)
- Uso de `re.IGNORECASE` para buscas case-insensitive
- Validação de formatos de dados (CPF, URL, nomes) com regex

## 🛠️ Tecnologias

- Python 3
- Módulo `re`

## ▶️ Como executar

```bash
python nome_do_arquivo.py
```

## 📚 Sobre

Parte do repositório [desafios-alura-python](https://github.com/wendellxavier0612-dotcom/desafios-alura-python), reunindo os exercícios do módulo de strings e expressões regulares do curso de Python da Alura.
