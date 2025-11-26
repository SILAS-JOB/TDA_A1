
# TDA_A1

Este repositório contém uma coleção de programas Python que demonstram vários conceitos fundamentais de programação. Cada programa está contido em seu próprio arquivo e serve a um propósito específico.

## Programas

*   **`src/con.py`**: Este programa solicita ao usuário a idade mínima para um evento e, em seguida, verifica se a idade do usuário atende ao requisito.
*   **`src/dict.py`**: Um sistema de cadastro de produtos que utiliza um dicionário para armazenar nomes e preços de produtos. O programa oferece um menu para adicionar e listar produtos.
*   **`src/list.py`**: Este programa coleta uma lista de nomes de alunos do usuário e os exibe após a conclusão da entrada.
*   **`src/ret.py`**: Este script demonstra duas maneiras de imprimir números pares de 1 a 100, uma usando um loop `for` e outra usando um loop `while`.

## Utilitários

*   **`src/utils/cl.py`**: Um módulo de utilidade simples que fornece uma função `clean()` para limpar a tela do terminal, compativel com Windows e outros sistemas operacionais.

## `.gitignore`

O arquivo `.gitignore` neste projeto foi gerado usando `npx gitignore python` e é configurado para ignorar arquivos e diretórios comuns do Python, como:

*   Arquivos de bytecode (`__pycache__/`, `*.pyc`)
*   Diretórios de distribuição (`build/`, `dist/`)
*   Arquivos de ambiente virtual (`.venv/`, `env/`)
*   Relatórios de teste e cobertura (`.coverage`, `htmlcov/`)

Isso garante que apenas o código-fonte essencial seja rastreado pelo Git, mantendo o repositório limpo e focado.

## Python com Tipagem Estrita vs. TypeScript

Neste projeto, foi feito um esforço para utilizar a tipagem estrita em Python, uma abordagem que está se tornando cada vez mais popular para melhorar a robustez e a manutenibilidade do código. Abaixo, uma análise comparativa em relação a linguagens como TypeScript:

### Python com Tipagem Estrita (`Type Hints`)

*   **Tipagem Gradual**: Python possui um sistema de tipagem gradual, o que significa que você pode introduzir tipos em seu código de forma incremental. Código sem anotações de tipo ainda é válido.
*   **Verificação em Tempo de Análise Estática**: As anotações de tipo em Python (type hints) não são impostas em tempo de execução por padrão. Elas são usadas por ferramentas de análise estática como `mypy`, `pyright` e `pytype` para detectar erros de tipo antes da execução.
*   **Sintaxe**: A sintaxe para anotações de tipo em Python é direta, usando dois pontos (`:`) após o nome da variável ou argumento e uma seta (`->`) para o tipo de retorno da função.

    ```python
    def somar(a: int, b: int) -> int:
        return a + b
    ```