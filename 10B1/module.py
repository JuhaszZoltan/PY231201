from random import randint
from math import sqrt

def feladat01(n:int) -> list[int]:
    lst:list[int] = []
    for _ in range(n):
        rsz:int = randint(10, 99)
        lst.append(rsz)
    return lst


def feladat02(lst:list[int]) -> None:
    for i in range(len(lst)):
        print(lst[i], end=' ')
        if (i+1) % 5 == 0:
            print(end='\n')


def feladat03(lst:list[int], n:int) -> int:
    db:int = 0
    for e in lst:
        if e % n == 0:
            db += 1
    return db


def feladat04(oszt:int) -> str:
    if oszt == 1: return 'elégtelen'
    elif oszt == 2: return 'elégésges'
    elif oszt == 3: return 'közepes'
    elif oszt == 4: return 'jó'
    elif oszt == 5: return 'jeles'
    else: return 'HIBÁS ÉRTÉK'


def feladat05(a:float, b:float) -> float:
    return sqrt(a*a + b*b)


def feladat06(lst:list[int]) -> list[int]:
    opl:list[int] = []
    for e in lst:
        if e % 5 == 0 and e not in opl:
            opl.append(e)
    opl.sort()
    return opl
