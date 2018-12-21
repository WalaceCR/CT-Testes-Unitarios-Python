from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao

class TestLeilao(TestCase):

    #método setUp que será invocado no início de todos os testes
    def setUp(self):
        # Cenário: 2 lances em ordem decrescente
        self.walace = Usuario("Walace")
        self.luana = Usuario("Luana")

        self.lance_da_Luana = Lance(self.luana, 150.00)
        self.lance_do_Walace = Lance(self.walace, 100.00)

        self.novoleilao = Leilao("Geladeira")

    def test_deve_retornar_menor_e_maior_valor_em_ordem_decrescente(self):

        self.novoleilao.propoe(self.lance_da_Luana)
        self.novoleilao.propoe(self.lance_do_Walace)

        # validação dos resultados
        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.novoleilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.novoleilao.maior_lance)

    def test_deve_retornar_menor_e_maior_valor_em_ordem_crescente(self):
        self.novoleilao.propoe(self.lance_da_Luana)
        self.novoleilao.propoe(self.lance_do_Walace)

        # validação dos resultados
        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.novoleilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.novoleilao.maior_lance)

    def test_deve_retornar_menor_e_maior_valor_com_mais_de_2_lances(self):
        # Cenário: compĺemento do cenário
        larissa = Usuario("larissa")

        lance_da_Larissa = Lance(larissa, 150.00)

        self.novoleilao = Leilao("Geladeira")
        self.novoleilao.propoe(self.lance_do_Walace)
        self.novoleilao.propoe(self.lance_da_Luana)
        self.novoleilao.propoe(lance_da_Larissa)

        # validação dos resultados
        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.novoleilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.novoleilao.maior_lance)

    def test_deve_retornar_menor_e_maior_valor_com_valores_iguais(self):
        # Cenário: compĺemento do cenário
        self.larissa = Usuario("larissa")

        self.lance_da_Larissa = Lance(self.larissa, 150.00)

        self.novoleilao = Leilao("Geladeira")

        self.novoleilao.propoe(self.lance_da_Luana)
        self.novoleilao.propoe(self.lance_do_Walace)
        self.novoleilao.propoe(self.lance_da_Larissa)

        # validação dos resultados
        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.novoleilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.novoleilao.maior_lance)

    def test_deve_retornar_maior_e_menor_lance_com_apenas_1_valor(self):
        # Cenário: compĺemento do cenário
        self.novoleilao.propoe(self.lance_da_Luana)

        # validação dos resultados
        menor_valor_esperado = 150.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.novoleilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.novoleilao.maior_lance)
