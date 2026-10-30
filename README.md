Atividade 09 — Teste de Software
Descrição

Este repositório contém os exercícios da Atividade 09 da disciplina de Teste de Software, com foco em:

Testes automatizados com Pytest.
Cobertura de instruções e de ramos.
Teste de mutação com Mutmut.
Análise de mutantes vivos e mortos.
Melhoria da qualidade da suíte de testes.
Tecnologias utilizadas
Python 3
Pytest
Pytest-Cov
Mutmut 3.8.0
Instalação

Clone o repositório:

bash
git clone URL_DO_REPOSITORIO


Entre na pasta do projeto:

bash
cd atividade_09


Instale as dependências:

bash
pip install -r requirements.txt

Exercícios
Exercício 01 — Classificação de alunos

Implementação de uma função para classificar alunos de acordo com a média e a frequência.

Foram realizados testes para verificar:

Aprovação.
Recuperação.
Reprovação.
Reprovação por falta.
Validação de média e frequência.

Também foram realizadas medições de cobertura e teste de mutação.

Exercício 02 — Carrinho de compras

Implementação de uma função para calcular o total de uma compra, aplicando desconto de 10% a partir do quarto produto.

Foram realizados testes para verificar:

Cálculo do total.
Aplicação de descontos.
Diferentes quantidades de produtos.
Valores decimais e arredondamento.

Também foram realizadas análises de cobertura de ramos e Mutation Score.

Como executar os testes

Para executar todos os testes:

bash
pytest -q


Para medir a cobertura de ramos:

bash
pytest -q --cov=carrinho_lib --cov-branch --cov-report=term-missing


No exercício 01, utilize o pacote correspondente:

bash
pytest -q --cov=classificacao_lib --cov-branch --cov-report=term-missing

Teste de mutação

Para executar o Mutmut:

bash
mutmut run


O resultado apresenta a quantidade de mutantes gerados, mortos e sobreviventes.

O Mutation Score é calculado por:

text
MS = (Mutantes mortos / Mutantes gerados) * 100

Objetivo da atividade

Avaliar a eficácia dos testes automatizados, comparando a cobertura de código com o Mutation Score e aprimorando a suíte de testes para identificar alterações no comportamento das funções.