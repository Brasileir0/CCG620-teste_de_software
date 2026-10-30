# 🧪 Atividade 09 — Teste de Software

> Repositório dedicado à resolução dos exercícios da Atividade 09 da disciplina de **Teste de Software**, com foco em engenharia de qualidade, cobertura de código e análise de mutação.

---

## 🎯 Objetivos da Atividade
* Implementar testes automatizados robustos utilizando o ecossistema **Pytest**.
* Mensurar e maximizar a cobertura de instruções e de ramos (**Branch Coverage**).
* Aplicar testes de mutação com o **Mutmut** para avaliar a eficácia real da suíte de testes.
* Analisar mutantes vivos e mortos para eliminar pontos cegos nas asserções.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python 3** | Linguagem base do projeto |
| **Pytest** | Framework de testes automatizados |
| **Pytest-Cov** | Ferramenta para análise e relatório de cobertura |
| **Mutmut** | Framework para execução de Testes de Mutação |

---

## 🚀 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone URL_DO_REPOSITORIO
   ```

2. **Entre na pasta do projeto:**
   ```bash
   cd CCG620-teste_de_software
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Estrutura dos Exercícios

### 👤 Exercício 01 — Classificação de Alunos
* **Contexto:** Validação de regras de negócio para classificar a situação acadêmica de alunos baseando-se em média ponderada e frequência mínima.
* **Cenários Testados:**
  * ✅ Aprovação regular
  * ⚠️ Recuperação
  * ❌ Reprovação por nota
  * 📉 Reprovação por falta (frequência insuficiente)
  * 🛑 Validação de limites (dados inválidos ou extremos)

### 🛒 Exercício 02 — Carrinho de Compras
* **Contexto:** Motor de cálculo de totalizadores de pedidos com aplicação de desconto progressivo (10% de desconto a partir do 4º item adicionado).
* **Cenários Testados:**
  * 🧮 Cálculo básico do total sem desconto
  * 🏷️ Aplicação correta do gatilho de desconto progressivo
  * 📦 Variação na quantidade de produtos e tratamento de bordas
  * 🪙 Validação de valores decimais, dízimas e regras de arredondamento

---

## 💻 Como Executar os Testes

### 🏃 Execução Simples
Para rodar todos os testes do projeto de forma limpa e resumida, acesse a pasta do exercício correspondente (`ex01` ou `ex02`) e execute:
```bash
pytest -q -o pythonpath=.
```

### 📊 Análise de Cobertura de Ramos (Branch Coverage)
Para extrair o relatório detalhado das linhas e caminhos lógicos que não foram cobertos pelos testes:

* **No Exercício 01:**
  ```bash
  pytest -q -o pythonpath=classificacao_lib --cov=src --cov-branch --cov-report=term-missing
  ```
* **No Exercício 02:**
  ```bash
  pytest -q -o pythonpath=carrinho_lib --cov=src --cov-branch --cov-report=term-missing
  ```

---

## 👾 Teste de Mutação (Mutmut)

O teste de mutação insere pequenas falhas intencionais no código sob teste (mutantes) para verificar se a sua suíte de testes é capaz de perceber a alteração e falhar (matando o mutante).

1. **Para executar a análise de mutação:**
   ```bash
   mutmut run
   ```

2. **Para visualizar o relatório final de mutantes sobreviventes:**
   ```bash
   mutmut results
   ```

### 📈 Métrica de Qualidade (Mutation Score)
O score final de mutação (**MS**) determina a eficiência real dos seus testes através da fórmula:

$$\text{Mutation Score (MS)} = \left( \frac{\text{Mutantes Mortos}}{\text{Mutantes Gerados}} \right) \times 100$$
