# TDA_A1

Este repositório contém uma coleção de programas Python que demonstram vários conceitos fundamentais de programação. Cada programa está contido em sua própria pasta.

---

## Exercício 1: Verificador de Idade (`con`)

Este programa solicita ao usuário a idade mínima para um evento e, em seguida, verifica se a idade do usuário atende ao requisito.

**Como executar:**

```bash
python3 con/con.py
```

**Exemplo de Entrada/Saída:**

```
Digite a idade mínima necessária para entrar no evento: 18
Digite a sua idade: 25
Aproveite o evento !
```

```
Digite a idade mínima necessária para entrar no evento: 18
Digite a sua idade: 17
Senhor vamos acionar a polícia.
```

---

## Exercício 2: Cadastro de Produtos (`dict`)

Um sistema de cadastro de produtos que utiliza um dicionário para armazenar nomes e preços de produtos. O programa oferece um menu para adicionar e listar produtos.

**Como executar:**

```bash
python3 dict/dict.py
```

**Exemplo de Entrada/Saída:**

```
Sistema para cadastro de produtos
1 - Adicionar produto
2 - Listar produtos
3 - Sair
Escolha uma opção: 
1
Digite o nome do produto: 
Banana
Digite o preço do produto: 
3,50
Produto Banana adicionado com sucesso!
```

```
Sistema para cadastro de produtos
1 - Adicionar produto
2 - Listar produtos
3 - Sair
Escolha uma opção: 
2
Produtos cadastrados: 

Produto: Banana - Preço: R$ 3.50
```

---

## Exercício 3: Lista de Alunos (`list`)

Este programa coleta uma lista de nomes de alunos do usuário e os exibe após a conclusão da entrada. O usuário pode digitar "exit" para parar de adicionar nomes.

**Como executar:**

```bash
python3 list/list.py
```

**Exemplo de Entrada/Saída:**

```
Escreva o nome dos alunos, ou exit para sair : 
Silas
Escreva o nome dos alunos, ou exit para sair : 
João
Escreva o nome dos alunos, ou exit para sair : 
exit
Nomes dos alunos: Silas, João
```

---

## Exercício 4: Números Pares (`ret`)

Este script demonstra duas maneiras de imprimir números pares de 1 a 100, uma usando um loop `for` e outra usando um loop `while`.

**Como executar:**

```bash
python3 ret/ret.py
```

**Exemplo de Saída:**

```
2
4
6
...
100
2
4
6
...
100
```

## Utilit�rios






*   **`src/utils/cl.py`**: Um m�dulo de utilidade simples que fornece uma fun��o `clean()` para limpar a tela do terminal, compativel com Windows e outros sistemas operacionais.





## `.gitignore`





O arquivo `.gitignore` neste projeto foi gerado usando `npx gitignore python` e � configurado para ignorar arquivos e diret�rios comuns do Python, como:





*   Arquivos de bytecode (`__pycache__/`, `*.pyc`)


*   Diret�rios de distribui��o (`build/`, `dist/`)


*   Arquivos de ambiente virtual (`.venv/`, `env/`)


*   Relat�rios de teste e cobertura (`.coverage`, `htmlcov/`)





Isso garante que apenas o c�digo-fonte essencial seja rastreado pelo Git, mantendo o reposit�rio limpo e focado.





## Python com Tipagem Estrita vs. TypeScript





Neste projeto, foi feito um esfor�o para utilizar a tipagem estrita em Python, uma abordagem que est� se tornando cada vez mais popular para melhorar a robustez e a manutenibilidade do c�digo. Abaixo, uma an�lise comparativa em rela��o a linguagens como TypeScript:





### Python com Tipagem Estrita (`Type Hints`)





*   **Tipagem Gradual**: Python possui um sistema de tipagem gradual, o que significa que voc� pode introduzir tipos em seu c�digo de forma incremental. C�digo sem anota��es de tipo ainda � v�lido.


*   **Verifica��o em Tempo de An�lise Est�tica**: As anota��es de tipo em Python (type hints) n�o s�o impostas em tempo de execu��o por padr�o. Elas s�o usadas por ferramentas de an�lise est�tica como `mypy`, `pyright` e `pytype` para detectar erros de tipo antes da execu��o.


*   **Sintaxe**: A sintaxe para anota��es de tipo em Python � direta, usando dois pontos (`:`) ap�s o nome da vari�vel ou argumento e uma seta (`->`) para o tipo de retorno da fun��o.





    ```python


    def somar(a: int, b: int) -> int:


        return a + b


    ```