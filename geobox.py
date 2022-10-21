# Esboço incipiente


import unittest


class GeodeticTechnique:
    def __init__(self, survey, read):
        self.read = read
        self.survey = survey

    def read_data(self, read):
        self.read = read
        return


class GeodeticTechniqueTest(unittest.TestCase):
    @staticmethod
    def test_technique():
        readed = GeodeticTechnique()
        assert isinstance(readed, GeodeticTechnique())


# 1) Arquivos e Diretórios temporários
"""
Para casos de n_leituras para o mesmo dia,
ou seja, n_arquivos para o mesmo dia de coleta,
utilizar o módulo nativo tempfile.TemporaryFile,
para criar diretórios temporários e
nome de arquivos temporários

1.1) Arquivo Temporário
from tempfile import TemporaryFile
with TemporaryFile('...') as f:
    # Read/Write/Rename to the file/directory
    f.seek('int', 'char', 'str')
    data = f.read()

1.2) Diretório Temporário
from tempfile import TemporaryDirectory
with TemporaryDirectory('...') as dirname:
    # Declarando qual o nome do diretório temporário
    print('dirname is:', dirname
"""

if __name__ == "__main__":
    unittest.main()
