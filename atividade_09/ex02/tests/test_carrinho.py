import pytest
from carrinho_lib.carrinho import total_com_desconto

def test_total_com_desconto():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0

    
def test_total_com_desconto_decimais():
    assert total_com_desconto([1.111, 2.222, 3.333]) == 6.67
