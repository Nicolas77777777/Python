import unittest
from unittest import TestCase
from Lezione20.gestionalepagamento import Pagamento, PagamentoContanti

class TestPagamaneto (TestCase):
    def setUp(self) -> None:

        self.pagamento:Pagamento= Pagamento()

        self.pagamento.setPagamento(30)

        self.pagamento.getPagamento()    

        self.pagamento.dettagliPagamento()