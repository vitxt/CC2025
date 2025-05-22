from enum import Enum,auto

class direcoes(Enum):
    LESTE=auto()
    SUL=auto()
    OESTE=auto()
    NORTE=auto()




def direcao_oposta(a:direcoes)->direcoes:
    '''
    >>> direcao_oposta(direcoes.LESTE).name
    'OESTE'
    >>> direcao_oposta(direcoes.OESTE).name
    'LESTE'
    >>> direcao_oposta(direcoes.SUL).name
    'NORTE'
    >>> direcao_oposta(direcoes.NORTE).name
    'SUL'
    
    '''
    if a==direcoes.LESTE:
        resposta=direcoes.OESTE
    elif a==direcoes.OESTE:
        resposta=direcoes.LESTE
    elif a==direcoes.SUL:
        resposta=direcoes.NORTE
    else:
        resposta=direcoes.SUL
    return resposta

def direcao_noventa_graus(b:direcoes)->direcoes:
    '''
    >>> direcao_noventa_graus(direcoes.LESTE).name
    'SUL'
    >>> direcao_noventa_graus(direcoes.SUL).name
    'OESTE'
    >>> direcao_noventa_graus(direcoes.OESTE).name
    'NORTE'
    >>> direcao_noventa_graus(direcoes.NORTE).name
    'LESTE'
    '''
    if b==direcoes.LESTE:
        resposta=direcoes.SUL
    elif b==direcoes.SUL:
        resposta=direcoes.OESTE
    elif b==direcoes.OESTE:
        resposta=direcoes.NORTE
    else:
        resposta=direcoes.LESTE
    return resposta

def direcao_menos_noventa_graus(c:direcoes)->direcoes:
    '''
    >>> direcao_menos_noventa_graus(direcoes.LESTE).name
    'NORTE'
    >>> direcao_menos_noventa_graus(direcoes.SUL).name
    'LESTE'
    >>> direcao_menos_noventa_graus(direcoes.OESTE).name
    'SUL'
    >>> direcao_menos_noventa_graus(direcoes.NORTE).name
    'OESTE'
    '''

    return direcao_noventa_graus(direcao_noventa_graus(direcao_noventa_graus(c)))

def quantos_graus(a:direcoes,b:direcoes)->int:
    '''
    >>> quantos_graus(direcoes.LESTE,direcoes.SUL)
    90
    >>> quantos_graus(direcoes.LESTE,direcoes.OESTE)
    180
    >>> quantos_graus(direcoes.LESTE,direcoes.NORTE)
    270
    >>> quantos_graus(direcoes.LESTE,direcoes.LESTE)
    0
    

    '''
    if direcao_noventa_graus(a)==b:
        res=90
    elif a==direcao_noventa_graus(b):
        res=180
    elif a==direcao_menos_noventa_graus(b):
        res=270
    else:
        res=0
    return res