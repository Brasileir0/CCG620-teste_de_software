> a) Meça a cobertura de ramos e rode o mutmut. Quantos mutantes foram gerados, mortos e vivos?
```
pytest -q -o pythonpath=. --cov=classificacao_lib --cov-branch --cov-report=term-missing
Name                                 Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------------
classificacao_lib/classificacao.py      12      4     10      4    64%   3, 5, 7, 11
tests/test_classificacao.py              5      0      0      0   100%
--------------------------------------------------------------------------------
TOTAL                                   17      4     10      4    70%

mutmut run
⠼ Generating mutants
    done in 211ms (1 files mutated, 0 ignored, 0 unmodified)
⠏ Running stats     
    done
⠦ Running clean tests
    done
⠹ Running forced fail test
    done
Running mutation testing
⠏ 36/36  🎉 6 🫥 0  ⏰ 0  🤔 0  🙁 30  🔇 0  🧙 0
10.79 mutations/second
```

Portanto, os resultados observados foram:
- Mutantes gerados/processados: 36
- Mutantes mortos: 6
- Mutantes vivos: 30

b) Agrupe os vivos pela causa e diga quais estão em linhas que a suíte nem executa
| Causa | Linhas relacionadas | Situação |
| - | - | - | 
| Validação da Média | 3 | Não executada |
| Validação da Presença | 5 | Não executada |
| Verificação da frequência mínima | 7 | Não executada |
| Verificação da média para aprovação e recuperação | 11 | Não executada | 

As linhas 3, 5, 7 e 11 não foram executadas pela suíte inicial, conforme o relatório de cobertura. Os mutantes relacionados a essas condições podem sobreviver justamente pela ausência de testes que exercitem esses caminhos. O agrupamento foi feito pelas causas identificadas no código, sem determinar a quantidade exata de mutantes por linha.

c) Acrescente testes até matar todos os vivos. Algum é equivalente? Qual o MS final?
| Resultado | Suite inicial | Suite ampliada |
| - | - | - | 
| Mutantes | 36 | 36 |
| Mortos | 6 | 30 |
| Vivos | 30 | 6 |
| Mutation Score | 16,67% | 83,33% |

Permaneceram seis mutantes vivos. Não foi possível confirmar se algum deles é equivalente, pois seria necessário analisar individualmente as alterações realizadas pelo Mutmut.

d) Troque a conferência da mensagem por pytest.raises(ValueError, match=msg). O que muda?
| Resultado | Letra C | Letra D |
| - | - | - | 
| Mutantes | 36 | 36 |
| Mortos | 30 | 28 |
| Vivos | 6 | 8 |
| Mutation Score | 83,33% | 77,78% | 
| Testes Aprovados | 11 | 11 |

Ao utilizar pytest.raises(ValueError, match=msg), a verificação da mensagem passa a utilizar expressão regular, em vez de comparar a mensagem completa por igualdade. Os 11 testes continuaram passando, mas o resultado da análise de mutação mudou: dois mutantes a menos foram mortos e o Mutation Score caiu de 83,33% para 77,78%. Isso demonstra que as duas formas de verificação podem produzir resultados diferentes.