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
    '''
    res = 0
    for n in lista:
        if n < lista[n]:
            
         
