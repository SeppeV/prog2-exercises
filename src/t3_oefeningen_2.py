import math


def is_even(x):
    """Geef True als x even is, anders False"""
    return True


def is_oneven(x):
    """Geef True als x oneven is, anders False"""
    # Implementeer deze functie gebruik makend van is_even
    return True

def oppervlakte_vierkant(zijde):
    resultaat = zijde ** 2
    return resultaat

def volume_kubus(zijde):
    resultaat = zijde ** 3
    if resultaat < 0:
        resultaat = 0
        return resultaat
    else:
        return resultaat

def volume_bol(r):
    """Return volume bol met straal r"""
    return 0


def oppervlakte_cirkel(r):
    resultaat = r ** 2 * math.pi
    return resultaat


def omtrek_cirkel(r):
    resultaat = 2 * r * math.pi
    return resultaat

def volume_cilinder(r, h):
    resultaat = math.pi * r ** 2 h
    return resultaat


def volume_donut(r, R):
    """Return volume donut met straal r en R
    waarbij r de dikte van de donut is, en R
    de grootte van de donut.
    """
    return 0


def stats(punten):
    """Return het gemiddelde, het maximum, het minimum en het aantal getallen
    als een lijst met punten gegeven werd."""
    return 0


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        """Return de omtrek van de cirkel met straal r"""
        return 0

    def oppervlakte(self):
        """Return de oppervlakte van de cirkel met straal r"""
        return 0

    def __str__(self):
        """Return een string zoals aangegeven in de testen"""
        return ""


def pythagoras(a, b):
    """Return de lengte van de schuine zijde als de lengtes
    van de rechthoekszijden gegeven zijn door a en b"""
    return 0


def is_palindroom(woord):
    """Return True als het omgekeerde van het woord gelijk
    is aan het woord zelf. Return anders False."""
    return True
