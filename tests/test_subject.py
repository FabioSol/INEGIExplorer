import pandas as pd

from inegi_explorer.nodes.subject_node import Subject
import unittest


class TestSubject(unittest.TestCase):
    def test_subject_bi(self):
        i1 = Subject("six", "0000", 6, {})
        assert i1.__repr__() == """Tema: six - Estados Unidos Mexicanos (T-0700-0000-6) 
    Tema: Demografía y Sociedad - Estados Unidos Mexicanos (T-0700-379-6)
    Tema: Economía y Sectores Productivos - Estados Unidos Mexicanos (T-0700-380-6)
    Tema: Geografía y Medio Ambiente - Estados Unidos Mexicanos (T-0700-381-6)
    Tema: Gobierno, Seguridad y Justicia - Estados Unidos Mexicanos (T-0700-382-6)"""
        assert i1[0].name == "Demografía y Sociedad"
        i2 = Subject("", "15", 6, {})
        d1=i2.fetch()
        assert isinstance(d1, pd.DataFrame)
        assert len(d1.columns)==43




    def test_subject_bie(self):
        i1 = Subject("zero", "0000", 0, {})
        assert i1.__repr__() == """Tema: zero - Estados Unidos Mexicanos (T-0700-0000-0) 
    Tema: Banco de Información Económica (BIE) - Estados Unidos Mexicanos (T-0700-999999999999-0)"""
        assert i1[0].name == "Banco de Información Económica (BIE)"
        i2 = Subject("", "1000008001800070", 0, {})
        d1 = i2.fetch()
        assert isinstance(d1, pd.DataFrame)
    def test_subject_IPEF(self):
        i1 = Subject("seven", "0000", 7, {})
        assert i1.__repr__() =="""Tema: seven - Estados Unidos Mexicanos (T-0700-0000-7) 
    Tema: Economía - Estados Unidos Mexicanos (T-0700-555-7)
    Tema: Educación - Estados Unidos Mexicanos (T-0700-552-7)
    Tema: Gobierno - Estados Unidos Mexicanos (T-0700-561-7)
    Tema: Población - Estados Unidos Mexicanos (T-0700-553-7)
    Tema: Salud - Estados Unidos Mexicanos (T-0700-550-7)
    Tema: Seguridad - Estados Unidos Mexicanos (T-0700-556-7)
    Tema: Trabajo - Estados Unidos Mexicanos (T-0700-551-7)
    Tema: Vivienda - Estados Unidos Mexicanos (T-0700-562-7)
    Tema: Calidad de vida - Estados Unidos Mexicanos (T-0700-563-7)"""
        i2= i1[0]
        assert i2.name == "Economía"
        d1 = i2.fetch()
        assert isinstance(d1, pd.DataFrame)



    def test_subject_IBPEF(self):
        i1 = Subject("", "0000", 8, {})
        assert i1.__repr__() =="""Tema:  - Estados Unidos Mexicanos (T-0700-0000-8) 
    Tema: Accesibilidad a servicios - Estados Unidos Mexicanos (T-0700-567-8)
    Tema: Relaciones sociales en la comunidad - Estados Unidos Mexicanos (T-0700-575-8)
    Tema: Educación - Estados Unidos Mexicanos (T-0700-569-8)
    Tema: Balance vida-trabajo - Estados Unidos Mexicanos (T-0700-574-8)
    Tema: Ingresos - Estados Unidos Mexicanos (T-0700-565-8)
    Tema: Medio Ambiente - Estados Unidos Mexicanos (T-0700-570-8)
    Tema: Compromiso cívico y gobernanza - Estados Unidos Mexicanos (T-0700-571-8)
    Tema: Salud - Estados Unidos Mexicanos (T-0700-572-8)
    Tema: Satisfacción con la vida - Estados Unidos Mexicanos (T-0700-573-8)
    Tema: Seguridad - Estados Unidos Mexicanos (T-0700-568-8)
    Tema: Empleo - Estados Unidos Mexicanos (T-0700-566-8)
    Tema: Vivienda - Estados Unidos Mexicanos (T-0700-564-8)"""
        i2=i1[0]
        assert i2.name == "Accesibilidad a servicios"
        d1=i2.fetch()
        assert isinstance(d1, pd.DataFrame)
        assert len(d1.columns) == 3




if __name__ == '__main__':
    unittest.main()
