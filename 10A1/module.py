from random import randint
from math import sqrt

# 1 ------------------
def feladat01(szam:int) -> list[int]:
    szamok:list[int] = []
    for _ in range(szam):
        rnd_szam = randint(10, 99)
        szamok.append(rnd_szam)
    return szamok

# 2 ------------------
def feladat02(lista:list[int]) -> None:
    for i in range(len(lista)):
        print(lista[i], end=' ')
        if (i+1) % 5 == 0:
            print(end='\n')

# 3 ------------------
def feladat03(lista:list[int], szam:int) -> int:
    db:int = 0
    for e in lista:
        if e % szam == 0:
            db += 1
    return db

# 4 ------------------
def feladat04(osztalyzat:int) -> str:
    if osztalyzat == 1: return 'elégtelen'
    elif osztalyzat == 2: return 'elégséges'
    elif osztalyzat == 3: return 'közepes'
    elif osztalyzat == 4: return 'jó'
    elif osztalyzat == 5: return 'jeles'
    else: return 'HIBÁS ÉRTÉK'

# 5 -----------------
def feladat05(a:float, b:float) -> float:
    return sqrt(a**2 + b**2)

# 6 -----------------
def feladat06(szamok:list[int]) -> list[int]:
    kimenet:list[int] = []
    for e in szamok:
        if e % 5 == 0 and e not in kimenet:
            kimenet.append(e)
    kimenet.sort()
    return kimenet
