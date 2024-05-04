import pandas as pd

from inegi_explorer.nodes.indicator_node import Indicator
import unittest


class TestIndicator(unittest.TestCase):
    def test_indicator_bi(self):
        i1 = Indicator("six", "8999999087", 6, {})
        assert i1.__repr__() == "Indicador: six - Estados Unidos Mexicanos (I-0700-8999999087-6)"

        d1 = i1.fetch()
        assert isinstance(d1, pd.Series)

        i2 = Indicator("", "1002000041", 6, {})
        assert [i.geographic_area_name for i in i2.get_children()] == ['Aguascalientes', 'Baja California',
                                                                       'Baja California Sur', 'Campeche',
                                                                       'Coahuila de Zaragoza', 'Colima', 'Chiapas',
                                                                       'Chihuahua', 'Ciudad de México', 'Durango',
                                                                       'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco',
                                                                       'México', 'Michoacán de Ocampo', 'Morelos',
                                                                       'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla',
                                                                       'Querétaro', 'Quintana Roo', 'San Luis Potosí',
                                                                       'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas',
                                                                       'Tlaxcala', 'Veracruz de Ignacio de la Llave',
                                                                       'Yucatán', 'Zacatecas']
        d2 = i2.fetch(agg=True)
        assert isinstance(d2, pd.DataFrame)

        d3 = i2[0].fetch()
        assert isinstance(d3, pd.Series)

        d4 = i2[0].fetch(agg=True)
        assert isinstance(d4, pd.DataFrame)

    def test_indicator_bie(self):
        i1 = Indicator("zero", "446735", 0, {})
        assert i1.__repr__() == "Indicador: zero - Estados Unidos Mexicanos (I-0700-446735-0)"
        d1 = i1.fetch()
        assert isinstance(d1, pd.Series)
        assert d1.name == "Población ocupada en el sector informal - Número de personas - Nacional"


    def test_indicator_IPEF(self):
        i1 = Indicator("seven", "6000000001", 7, {})
        assert isinstance(i1.fetch(), pd.Series)
        assert isinstance(i1[0].fetch(), pd.Series)
        assert isinstance(i1.fetch(agg=True), pd.DataFrame)

    def test_indicator_IBPEF(self):
        i1 = Indicator("", "6200108755", 8, {})
        assert isinstance(i1.fetch(), pd.Series)
        assert isinstance(i1[0].fetch(), pd.Series)
        assert isinstance(i1.fetch(agg=True), pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
