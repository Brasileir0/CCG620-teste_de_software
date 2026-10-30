
import pytest
from classificacao_lib.classificacao import classificar_aluno


@pytest.mark.parametrize(
    "media, presenca, esperado",
    [
        (8.0, 80, "Aprovado"),
        (3.0, 90, "Reprovado"),
        (6.0, 80, "Recuperacao"),
        (8.0, 74, "Reprovado por falta"),
        (7.0, 75, "Aprovado"),
        (5.0, 75, "Recuperacao"),
        (4.9, 75, "Reprovado"),
    ],
)
def test_classificar_aluno(media, presenca, esperado):
    assert classificar_aluno(media, presenca) == esperado


@pytest.mark.parametrize(
    "media, presenca, msg",
    [
        (-1, 80, "Media invalida"),
        (11, 80, "Media invalida"),
        (8, -1, "Presenca invalida"),
        (8, 101, "Presenca invalida"),
    ],
)
def test_valores_invalidos(media, presenca, msg):
    with pytest.raises(ValueError, match=msg):
        classificar_aluno(media, presenca)