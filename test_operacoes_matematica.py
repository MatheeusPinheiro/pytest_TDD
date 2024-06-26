from Model.Matematica import OperacoesMatematica
import pytest




class TesteOperacoes:
    def setup_method(self):
        """Configuração antes de cada método de teste."""
        self.calc = OperacoesMatematica()

    def test_somar(self):
        resultado = self.calc.somar(1, 2)
        assert resultado == 3

    def test_subtrair(self):
        resultado = self.calc.subtrair(5, 3)
        assert resultado == 2

    def test_adicionar_negativos(self):
        resultado = self.calc.somar(-1, -1)
        assert resultado == -2

    def test_subtrair_negativos(self):
        resultado = self.calc.subtrair(-1, -1)
        assert resultado == 0

    def test_adicionar_zero(self):
        resultado = self.calc.somar(0, 0)
        assert resultado == 0

    def test_subtrair_zero(self):
        resultado = self.calc.subtrair(0, 0)
        assert resultado == 0