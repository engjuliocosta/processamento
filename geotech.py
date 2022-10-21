""" Geodetic Technique """


class Sat:
    __slots__ = ['elev', 'azim']

    def __init__(self, elev: object, azim: object) -> None:
        self.elev = elev
        self.azim = azim


class Reflectometry:
    __slots__ = ['station', 'year', 'doys', 'coord', 'height']

    def __init__(self, station: object, year: object, doys: object, coord: object, height: object) -> None:
        self.station = station
        self.year = year
        self.doys = doys
        self.coord = coord
        self.height = height


def test_reflec():
    stack = Reflectometry()
    assert isinstance(stack, Reflectometry)
    assert stack.station == 'sph1'
    assert stack.year == 2019
    assert stack.doys == {'doy': 235, 'doy_end': 242}
    assert stack.coord == {'lat': -30.1415, 'long': -50.3456}
    assert stack.height == {'h1': 1.3, 'h2': 3.8}


def test_satelite():
    prm = Sat({'e1': 5.0, 'e2': 15.0}, {'a1': 201, 'a2': 300})
    assert isinstance(prm, Sat)
    assert prm.elev == {'e1': 5.0, 'e2': 15.0}
    assert prm.azim == {'a1': 201, 'a2': 300}


# Rever vídeo para invocar Classes e métodos, funções

# Boa prática de resolução do problema

"""
Abordagem adotada:
    - Classe Satélite: atributos (elevação, azimute)
    - Classe Refletometria: 
        atributos (estação; 
                   ano da observação; 
                   dias {dia inicial, dia final}; 
                   coordenadas {latitude, Longitude}; 
                   altura {altura inicial, altura final} )
        * Classe Refletometria pode ser extendida a partir de Classe técnica, posteriormente.
    Esboço inicial
    
    Vai receber pacote gnssrefl para tratar os dados
"""

"""
Criar uma outra classe Dados_Geodeśicos?
"""
