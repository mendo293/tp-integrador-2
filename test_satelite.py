import pytest
from satelite import Satelite

def test_satelite_valido():
    sat = Satelite("ISS", 25544, -41.0, -71.0, 400)
    assert sat.nombre == "ISS"
    assert sat.tipo_orbita() == "LEO"
    assert sat.en_zona(-80, -50, -60, -30) is True

def test_satelite_invalidos():
    with pytest.raises(ValueError):
        Satelite("", 1, 0, 0, 500)
    with pytest.raises(ValueError):
        Satelite("SAT", 1, 100, 0, 500)
    with pytest.raises(ValueError):
        Satelite("SAT", 1, 0, 0, 50)