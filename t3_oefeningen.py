import math


def bmi(gewicht, lengte):
    if gewicht <= 0:
        return -1
    elif lengte <= 0:
        return -1
    else:
        resultaat = gewicht / (lengte ** 2)
        return resultaat


def omtrek_cirkel(r):
    resultaat = 2 * r * math.pi
    if r <= 0:
        return -1
    else:
        return resultaat


def oppervlakte_cirkel(r):
    resultaat = r ** 2 * math.pi
    if r <= 0:
        return -1
    else:
        return resultaat


def oppervlakte_vierkant(zijde):
    resultaat = zijde ** 2
    if zijde <= 0:
        return -1
    elif resultaat <= 0:
        return -1
    else:
        return resultaat


def volume_cilinder(r, h):
    resultaat = math.pi * r ** 2 * h
    if r <= 0:
        return -1
    elif h <= 0:
        return -1
    else:
        return resultaat


def volume_kubus(zijde):
    resultaat = zijde ** 3
    if resultaat < 0:
        resultaat = 0
        return resultaat
    else:
        return resultaat