import math


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_oneven(x):
    resultaat = is_even(x)
    if resultaat == True:
        return False
    else:
        return True


def volume_bol(r):
    if r < 0:
        return -1
    else:
        resultaat = (4/3) * pi * r**3
        return resultaat


def oppervlakte_cirkel(r):
    if r < 0:
        return -1
    else:
        resultaat = pi * r**2
        return resultaat


def omtrek_cirkel(r):
    if r < 0:
        return -1
    else:
        resultaat = 2 * r * pi
        return resultaat


def volume_donut(r, R):
    if r < 0:
        return -1
    elif R < 0:
        return -1
    elif r == R:
        return -1
    else:
        resultaat = 2 * pi**2 * r**2 * R
        return resultaat


def stats(punten):
    gemiddelde = sum(punten) / len(punten)
    maximum = max(punten)
    minimum = min(punten)
    aantal = len(punten)
    return gemiddelde, maximum, minimum, aantal


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        result = pi * 2 * self.straal
        return result

    def oppervlakte(self):
        result = self.straal**2 * pi
        return result

    def __str__(self):
        return f"cirkel van de straal is {self.straal}"


def pythagoras(a, b):
    if a < 0:
        return -1
    elif b < 0:
        return -1
    else:
        regel = (a**2) + (b**2)
        resultaat = (regel)
        return resultaat


def is_palindroom(woord):
    def isPalindroom(s):
        return s == s[::-1]
    ans = isPalindroom(woord)
    return ans