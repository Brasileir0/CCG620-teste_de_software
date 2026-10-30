a) Meça a cobertura de ramos e o MS. O que os dois números dizem sobre a suíte?

```
pytest -q --cov=carrinho_lib --cov-branch --cov-report=term-missing
.                                                                                                                                                                                                                  [100%]
===================================================================================================== tests coverage =====================================================================================================
____________________________________________________________________________________ coverage: platform linux, python 3.14.2-final-0 _____________________________________________________________________________________

Name                       Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------
carrinho_lib/carrinho.py       7      0      4      0   100%
----------------------------------------------------------------------
TOTAL                          7      0      4      0   100%
1 passed in 0.04s

mutmut run
⠼ Generating mutants
    done in 449ms (1 files mutated, 0 ignored, 0 unmodified)
⠇ Running stats     
    done
⠼ Running clean tests
    done
⠋ Running forced fail test
    done
Running mutation testing
⠧ 16/16  🎉 4 🫥 0  ⏰ 0  🤔 0  🙁 12  🔇 0  🧙 0
9.90 mutations/second
```
| Métrica | Resultado |
| - | - |
| Instruções | 7 |
| Instruções não executadas | 0 |
| Ramos | 4 |
| Ramos parcialmente cobertos | 0 |
| Cobertura | 100% |

MS = 4/16 * 100 = 25%

A cobertura de ramos foi de 100%, indicando que todos os caminhos da função foram executados. Entretanto, o Mutation Score foi de apenas 25%, demonstrando que, apesar de executar todos os caminhos, a suíte inicial não conseguia detectar a maioria das alterações no comportamento do programa

b) Troque só o assert pelo valor exato, sem mudar a entrada. Quantos vivos restam?

```
mutmut run
⠼ Generating mutants
    done in 138ms (1 files mutated, 0 ignored, 0 unmodified)
⠇ Running stats     
    done
⠼ Running clean tests
    done
⠋ Running forced fail test
    done
Running mutation testing
⠧ 16/16  🎉 13 🫥 0  ⏰ 0  🤔 0  🙁 3  🔇 0  🧙 0
7.77 mutations/second
```

| Resultado | Antes | Depois |
| - | - | - |
| Mutantes gerados | 16 | 16 |
| Mortos | 4 | 13 |
| Vivos | 12 | 3c |
| Mutation Score | 25% | 81,25% |

MS = 13/16 * 100 = 81,25%

Após substituir o assert genérico pelo valor exato esperado (141.0), restaram apenas 3 mutantes vivos. O Mutation Score aumentou de 25% para 81,25%, mostrando que uma asserção mais específica consegue identificar mais alterações no comportamento da função.

c) Para cada vivo que restou, diga qual condição falhou: alcançar, infectar, propagar ou revelar

| Condição | Resultado |
| - | - |
| Alcançar | Sim. A instrução return é executada. |
| Infectar | Não com essa entrada: as alterações não produzem diferença numérica detectável |
| Propagar | Não há diferença observável para propagar. |
| Revelar | Não. O assert aceita os resultados dos mutantes. |

Os três mutantes sobrevivem porque a entrada utilizada produz um resultado inteiro (141.0), não permitindo identificar as diferenças provocadas pelas alterações na função de arredondamento.

d) Acrescente as entradas que faltam até o MS chegar a 100%. Que tipo de preço foi preciso?

| Entrada adicionada:
```python
def test_total_com_desconto_decimais():
    assert total_com_desconto([1.111, 2.222, 3.333]) == 6.67
```

```
mutmut run
⠼ Generating mutants
    done in 263ms (1 files mutated, 0 ignored, 0 unmodified)
⠏ Running stats     
    done
⠦ Running clean tests
    done
⠹ Running forced fail test
    done
Running mutation testing
⠏ 16/16  🎉 16 🫥 0  ⏰ 0  🤔 0  🙁 0  🔇 0  🧙 0
13.81 mutations/second
```

MS = 16/16 * 100 = 100%

Foram acrescentados testes com valores decimais para verificar o comportamento do arredondamento. A nova entrada permite identificar diferenças entre arredondar para duas casas decimais, para um número inteiro ou para três casas decimais. Com isso, os três mutantes sobreviventes podem ser eliminados. O objetivo é alcançar 100% de Mutation Score, sem mutantes vivos.