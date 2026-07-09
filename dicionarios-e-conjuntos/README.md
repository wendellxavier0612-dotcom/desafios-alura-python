# Conjuntos e Dicionários

Exercícios práticos do módulo de **conjuntos (`set`)** e **dicionários (`dict`)** em Python, parte do curso da [Alura](https://www.alura.com.br/).

## 📂 Exercícios

### 📖 Dicionários
- **analise_participantes.py** — Percorre um dicionário exibindo nomes e idades de participantes.
- **analise_vendas.py** — Calcula o total de vendas por categoria, com dicionário de listas de dicionários (estrutura aninhada).
- **atualizando_estoque.py** — Atualiza a quantidade de um produto já existente em um dicionário de estoque.
- **cadastro_produtos.py** — Cadastra produtos e quantidades em um dicionário.
- **organizando_lista_convidados.py** — Adiciona convidados a um dicionário até o usuário digitar "sair".

### 🔗 Conjuntos
- **comparar_conjunto_números.py** — Une dois conjuntos de tarefas (`union`) e remove um item específico.
- **comparar_listas.py** — Compara dois conjuntos de itens, identificando itens exclusivos (`difference`) e em comum (`intersection`).
- **descobrindo_palavras_comuns.py** — Encontra palavras em comum entre dois textos usando `intersection`.
- **gerenciamento_incrições.py** — Remove um participante de múltiplos conjuntos de inscritos em workshops (`discard`).
- **verificar_permissoes.py** — Verifica se as permissões solicitadas fazem parte das permissões principais, usando `difference`.

## 🛠️ Conceitos praticados

- Dicionários: criação, leitura, atualização de valores, iteração com `.keys()`, `.values()`, `.items()`
- Conjuntos: `.union()`, `.intersection()`, `.difference()`, `.add()`, `.discard()`, `.remove()`
- Diferença entre `.discard()` (não gera erro se o item não existir) e `.remove()` (gera `KeyError`)
- Tratamento de exceções (`try/except`) para entradas inválidas
- Funções recursivas para repetir uma entrada até ser válida

## 🛠️ Tecnologias

- Python 3

## ▶️ Como executar

```
python nome_do_arquivo.py
```

## 📚 Sobre

Parte do repositório [desafios-alura-python](https://github.com/wendellxavier0612-dotcom/desafios-alura-python), reunindo os exercícios do módulo de conjuntos e dicionários do curso de Python da Alura.
