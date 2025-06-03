def concatenador (lst:list):
    '''
    >>> concatenador (['asf','usdiuhf','asdoif'])
    'asfusdiuhfasdoif'
    '''
    res = ''
    for n in lst:
        res = res + n
    return res


def cria_lista (strings:list):
    '''
    >>> cria_lista(['oi','tchau','hello'])
    [2, 5, 5]
    '''
    nums = []
    for n in strings:
        nums.append(len(n))
    return nums

def produto (inteiros:list):
    '''
    >>> produto([2,3,1,2])
    12
    '''
    assert len(inteiros) != 0
    res = 1
    for n in inteiros:
        res = res*n
    return res 

def saoPares (inteiros:list):
    '''
    >>> saoPares([1,2,3,4])
    False
    >>> saoPares([2,4,6,22])
    True
    '''
    res = True
    for n in inteiros:
        if n%2 == 1:
            res = False
    return res

def saoFalsos (bools : list):
    '''
    >>> saoFalsos([False,False,False])
    True
    >>> saoFalsos([False,True])
    False
    '''
    res = True
    for n in bools:
        if n == True:
            res = False
    return res

def retiraZeros (lista:list):
    '''
    >>> retiraZeros([2,4,3,6,0,87,0])
    [2, 4, 3, 6, 87]
    >>> retiraZeros([0,0])
    []
    '''
    res = []
    for n in lista:
        if n != 0:
            res.append(n)
    return res

def quantosMin (lista:list):
    '''
    >>> quantosMin([1,23,5,4,1,1])
    3
    >>> quantosMin([0,0,32,4,3,0])
    3
    >>> quantosMin([21,2,32,4,3,2,4,76,2])
    3
    '''
    
    min = lista[0]

    for n in lista:
        if n<=min:
            min = n
    
    res = 0

    for a in lista:
        if min == a:
            res = res + 1


    return res



def amplitude (lista:list):
    '''
    >>> amplitude([2,4,12,5,2,10])
    10
    >>> amplitude([-1,32,-23,2])
    55
    '''
    max = lista[0]
    min = lista[0]
    for i in lista:
        if i > max:
            max = i
    for i in lista:
        if i < min:
            min = i
    return max - min 

from enum import Enum,auto

class sinal(Enum):
    POSITIVO=auto()
    NEGATIVO=auto()


def mais_posi_ou_nega (lista:list):
    '''
    >>> mais_posi_ou_nega([2,3,1,2,-2,-3,-23,1]).name
    'POSITIVO'
    >>> mais_posi_ou_nega([2,2,34,-12,-12,-2])
    ''
    '''

    res = 0
    for n in lista:
        if n < 0:
            res -=1
        else:
            res +=1
    if res > 0:
        res= sinal.POSITIVO
    elif res < 0:
        res = sinal.NEGATIVO
    else:
        res = ''
    return res



def neg_antes (lista:list):
    '''
    >>> neg_antes([21,4,3,-2,-21])
    [-2, -21, 21, 4, 3]
    '''
    res = []
    for i in lista:
        if i < 0:
            res.append(i)
    for i in lista:
        if i > 0:
            res.append(i)
    return res


def remove_negativo(a:list):
    '''
    >>> remove_negativo([2,12,323,1,-12,12,-9])
    [2, 12, 323, 1, 12]
    
    
    '''
    
    for n in a:
        if n < 0:
            a.remove(n)
    return a     



def movimento (posicao:list,movs:list):
    '''
    >>> movimento([1,3,10],[2,-4,1])
    [3, -1, 11]
    
    '''
    a = 0
    res = []
    for i in posicao:
        res.append(i + movs[a])
        a+=1
    return res

def quanto_doar (saldo_inicial:int,historico:list):
    '''
    >>> quanto_doar(100,[20,30,-40,-60,-50,30,-50,90,10,-200])
    20
    '''
    doar = 0
    for i in historico:
        saldo_inicial = saldo_inicial + i
        if saldo_inicial<0:
            doar+=10
    return doar


from dataclasses import dataclass


@dataclass
class desempenho:
    vitorias:int
    pontos:int
    saldo:int

def desempenho_ (res:list)->desempenho:
    '''
    >>> desempenho_([(2,1),(1,5),(3,3),(6,2)])
    desempenho(vitorias=2, pontos=7, saldo=1)
    '''
    sal = 0
    pont = 0
    vit = 0
    for i,n in res:
        sal+=i
        sal-=n
        if i>n:
                vit+=1
                pont+=3
        if i == n:
                pont+=1 

    return desempenho(vit,pont,sal)


def laurea (a:list):
    '''
    >>> laurea([9,6,10,9,9,5,7,9,10,7,9,10])
    True
    '''
    sim = 0
    res = False
    for i in a:
        if i >=9:
            sim+=1
    if sim>=(2/3)*len(a):
        res = True
    return res


from enum import Enum,auto

class votos(Enum):
    PRIMEIRO=(auto)
    SEGUNDO=(auto)
    NOVA_ELEICAO=(auto)

    

def election (a:list):
    '''
    >>> election([1,2,0,2,0,1,2,1,2,2,0]).name
    'SEGUNDO'
    >>> election([0,0,2,0,1,0,0,2,2,0]).name
    'NOVA_ELEICAO'
    >>> election([1,2,0,2,0,1,2,1,2,2,0,1,1,1,1,1,1,1]).name
    'PRIMEIRO'
    '''
    prim = 0
    seg = 0
    bran = 0
    for n in a:
        if n == 1:
            prim=prim +1
        if n == 2:
            seg =seg +1
        if n == 0:
            bran =bran +1
    if bran > len(a) / 2:
        return votos.NOVA_ELEICAO
    elif prim > seg:
        return votos.PRIMEIRO
    elif seg > prim:
        return votos.SEGUNDO
    else:
        return votos.NOVA_ELEICAO
    
  
        
