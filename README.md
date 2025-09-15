# 🧮 Calculator-Pytest

Um projeto de estudo para demonstrar a implementação de uma classe `Calculadora` em Python, com foco em **desenvolvimento orientado a testes (TDD)** utilizando o framework **pytest**.

O principal objetivo é aplicar boas práticas de teste, incluindo a organização da suíte de testes com **marcadores (markers)** para uma execução granular e controlada.

A calculadora implementa:

- 🟢 **4 operações básicas:** adição, subtração, multiplicação e divisão  
- ⚡ **2 operações extras:** potenciação e radiciação (raiz quadrada)

---

### ⚙️ Instalação do ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

**1. Clone o repositório:**
```bash
git clone https://github.com/sabsfreitas/calculator-pytest
cd calculator-pytest
```

**2. Crie e ative um ambiente virtual:**
```python -m venv .venv```

**No Linux/macOS:**
```source .venv/bin/activate```

**No Windows**:
```.venv\Scripts\activate```

**3. Instale as dependências:**
```pip install -r requirements.txt```

## 🧪 Executando os Testes
Com o ambiente configurado, você pode executar a suíte de testes de diferentes formas.

**1. Executar todos os testes:**
Para rodar todos os testes com o máximo de detalhes:
```pytest -v```

**2. Executar testes por marcadores (markers):**
Os testes foram categorizados com marcadores (markers) para permitir a execução de grupos específicos.

* Operações básicas

    ```pytest -m operacoes_basicas -v```


* Extras (radiciação e potenciação)

    ```pytest -m extras -v```


* Exceções

    ```pytest -m excecoes -v```


* Smoke tests

    ```pytest -m smoke -q```
