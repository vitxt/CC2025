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
    elif direcao_noventa_graus(a)==direcao_menos_noventa_graus(b):
        res=180
    elif a==direcao_noventa_graus(b):
        res=270
    else:
        res=0
    return res


class elevador(Enum):
    PARADO=auto()
    SUBINDO=auto()
    DESCENDO=auto()

def situacao (andar_atual:int,andar_final:int)->elevador:
    '''
    >>> situacao (0,3).name
    'SUBINDO'
    >>> situacao (3,1).name
    'DESCENDO'
    >>> situacao (0,0).name
    'PARADO'

    '''
    if andar_atual<andar_final:
        res = elevador.SUBINDO
    elif andar_final==andar_atual:
        res = elevador.PARADO
    else:
        res= elevador.DESCENDO    
    return res










from dataclasses import dataclass


@dataclass
class data:
    dia:int
    mes:int
    ano:int


def converte (a:str)->data:
    '''
    >>> converte ("21/01/2006")
    data(dia=21, mes=1, ano=2006)
    '''
    d=int(a[0:2])
    m=int(a[3:5])
    Ano=int(a[6:])
    return data(d,m,Ano)

def ultimo_dia (a:data)->bool:
    '''
    >>> ultimo_dia (data(20,3,2000))
    False
    >>> ultimo_dia (data(31,12,2006))
    True
    '''
    if a.mes==12 and a.dia==31:
            res=True
    else:res=False

    return res

def vem_antes (a:data,b:data)->bool:
    '''
    >>> vem_antes(data(20,3,2000),data(21,2,1999))
    False
    >>> vem_antes(data(21,2,1200),data(13,3,1300))
    True
    >>> vem_antes(data(21,2,1200),data(13,3,1200))
    True
    >>> vem_antes(data(21,2,1200),data(12,2,1200))
    False
    '''
    if a.ano<b.ano:
        res=True
    elif a.ano==b.ano:
        if a.mes<b.mes:
            res=True
        else:
            if a.dia<b.dia:
                res=True
            else:
                res=False
    else:
        res=False

    return res


@dataclass
class resolucao:
    altura:int
    largura:int

def quantos_mpx (a:resolucao)->float:
    '''
    >>> quantos_mpx(resolucao(1000,1000))
    1.0
    '''
    return (a.altura*a.largura)/1000000

class aspecto(Enum):
    QUATRO_POR_TRES=(auto)
    DEZESSEIS_POR_NOVE=(auto)

def qual_aspecto (a:resolucao)->aspecto:
    '''
    >>> qual_aspecto(resoluco(1920,1080))
    'DEZESSEIS_POR_NOVE'


    '''    
