from unittest import TestCase
import main 
import datetime
import pytest
import requests
from mock import patch

class TestART(TestCase):

    def test_single_art_status_code(self):
        """
            TESTE DE RETORNO DO status_code DE UMA REQUISIÇÃO NO SITE DO CREA-RJ
        """
        art_number = 560
        url = requests.head(f"https://portalservicos.crea-rj.org.br/rest-api/crea/art/detalhado/{art_number}")
        self.assertEqual(200, url.status_code)

    def test_raw_valid_art_number_data_return(self):
        raw_art_data_keys = str(main.collect_raw_art_data("560").keys())
        expected_keys = "dict_keys(['numero', 'descricaoFatoGerador', 'numeroArtPrincipal', 'numeroArtParticipacaoTecnica', 'cancelada', 'baixada', 'dataBaixa', 'motivoBaixaOutros', 'haEmpresaVinculada', 'haProfissionalCoResponsavel', 'dataCadastro', 'dataCadastroFormatada', 'dataPagamentoFormatada', 'dataReprocessamentoExigencia', 'forma', 'funcionarioCadastro', 'funcionarioAlteracao', 'protocolo', 'protocoloDevolucao', 'codigoLiberacao', 'tipoTaxa', 'formaRegistro', 'pessoaOutEstPais', 'isOnline', 'pagouPrazo', 'dataPagamento', 'dataUltimaAlteracao', 'dataEmailCobranca', 'isOEPaisLiberacao', 'valorPago', 'valorReceber', 'isAcaoOrdinaria', 'atual', 'isEmpresa', 'isEmpresaLiberacao', 'isEmpresaStatusLiberacao', 'isTermoAditivo', 'finalizada', 'liberada', 'exigencia', 'acessibilidade', 'assinaturaContratado', 'usuarioCadastro', 'isCertificada', 'isResgate', 'is1025', 'isOutEstPais', 'pagouNoPrazo', 'isOutEstPaisStatusLiberacao', 'estaQuitada', 'multiplaMensal', 'vinculoContratual', 'webService', 'quantidadeContratos', 'natureza', 'tipo', 'participacaoTecnica', 'fatoGerador', 'entidadeClasse', 'baixaArt', 'profissional', 'empresa', 'contrato', 'dadosContratoAnalise', 'contratos', 'modelo', 'descricaoModelo', 'contratoArt', 'possuiContratoCadastrado', 'primeiraParticipacaoTecnica'])"
        self.assertEqual(raw_art_data_keys, expected_keys)

    def test_raw_invalid_art_number_data_return(self):
        raw_art_data = main.collect_raw_art_data("1")
        expected_return = "Dados crus da ART 1 não encontrados."
        self.assertEqual(raw_art_data, expected_return)

    def mocked_test(self):
        expected_companies_amount = 5
        self.assertEqual(main.companies_list_for_mock_test.companies_list, expected_companies_amount)