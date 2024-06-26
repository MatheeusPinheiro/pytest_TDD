import pytest
from main import somar_dois_numeros



def test_soma_da_funcao_soma_dois_numeros():
    assert somar_dois_numeros(9,4) == 13