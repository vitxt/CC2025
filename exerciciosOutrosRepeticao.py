def encontrar_posicoes_nome(lst,nome):
    '''
    Examples:
    >>> nomes = ["ana", "bruno", "carla", "ana", "daniel", "ana"]
    >>> encontrar_posicoes_nome(nomes, "ana")
    [0, 3, 5]

    >>> nomes = ["fernanda", "gustavo", "helena", "igor"]
    >>> encontrar_posicoes_nome(nomes, "gustavo")
    [1]

    >>> nomes = ["joão", "maria", "josé"]
    >>> encontrar_posicoes_nome(nomes, "pedro")
    []

    >>> lista_vazia = []
    >>> encontrar_posicoes_nome(lista_vazia, "ana")
    []

    >>> nomes_case = ["Maria", "maria", "MARIA"]
    >>> encontrar_posicoes_nome(nomes_case, "maria")
    [1]

    >>> nomes_repetidos = ["paulo", "paulo", "paulo"]
    >>> encontrar_posicoes_nome(nomes_repetidos, "paulo")
    [0, 1, 2]
    '''
    res = []
    for n in range(0,len(lst)):
        if lst[n] == nome:
            res.append(n)
    return res

def remover_da_lista_por_posicao(lst:list,posicao):
    '''
    Examples:
    >>> remover_da_lista_por_posicao([10, 20, 30, 40, 50], 2)
    [10, 20, 40, 50]

    >>> remover_da_lista_por_posicao([99, 88, 77], 0)
    [88, 77]

    >>> remover_da_lista_por_posicao([5, 10, 15, 20], 3)
    [5, 10, 15]

    >>> remover_da_lista_por_posicao([1, 2, 3, 4, 5], -1)
    [1, 2, 3, 4]

    >>> remover_da_lista_por_posicao([1, 2, 3, 4, 5], -2)
    [1, 2, 3, 5]

    '''
    
    lst.remove(lst[posicao])
    return lst

def nova_lista(lst:list,i,n):
    '''
    Examples:
    >>> nova_lista([10, 20, 40, 50], 2, 30)
    [10, 20, 30, 40, 50]

    >>> nova_lista([10, 20, 30], 0, 5)
    [5, 10, 20, 30]


    '''
    
    res = []
    index = 0
    for ele in lst:
        if index != i:
            res.append(ele)
        else:
            res.append(n)
            res.append(ele)
        index+=1
        
    return res


def rotaciona (lst:list,n):
    '''
    Exemplos:
    >>> rotaciona([5, 3, 4, 1, 7], 2)
    [4, 1, 7, 5, 3]

    >>> rotaciona([1, 2, 3, 4, 5], 0)
    [1, 2, 3, 4, 5]

    >>> rotaciona([1, 2, 3, 4, 5], 5)
    [1, 2, 3, 4, 5]

    >>> rotaciona([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    '''
    res = []
    if n ==0 or n==len(lst):
        res = lst
    else:
        for a in range(0,len(lst)):
            if a >= n:
                res.append(lst[a])
        for a in range(0,len(lst)):
            if a < n:
                res.append(lst[a]) 
    return res

def dobrada(lst:list):
    '''
    Exemplos:
    >>> dobrada([1, 2, 1, 2])
    True

    >>> dobrada([3, 3])
    True

    >>> dobrada([1, 2, 3, 1, 2])
    False

    >>> dobrada([0, 0, 0, 0])
    True
    '''
    assert len(lst)!= 0 
    i = 0
    j = len(lst) // 2
    res = True
    while res and j!=len(lst):
        if lst[i] != lst[j]:
            res = False
        i+=1
        j+=1
    return res


'''Projete uma função que determine qual é a menor quantidade de elementos de uma lista que precisam
ser somados (a partir do início da lista) para que a soma seja maior que um dado valor. Se não for
possível atingir a soma desejada, a função deve devolver -1'''

def menor_quantidade (lst:list,n):
    '''
    >>> menor_quantidade([1, 2, 3, 4], 6)
    4
    >>> menor_quantidade([1, 1, 1, 1], 5)
    -1
    >>> menor_quantidade([], 0)
    -1
    >>> menor_quantidade([5, 5, 5], 5)
    2
    >>> menor_quantidade([2, 4, 6, 8], 7)
    3
    >>> menor_quantidade([10], 5)
    1
    >>> menor_quantidade([10], 15)
    -1
    >>> menor_quantidade([0, 0, 0, 1], 1)
    -1
    '''
    elementos = 0
    soma = 0
    for a in lst:
        if soma <= n:
            soma += a
            elementos += 1
    if soma <= n:
        elementos = -1    


    return elementos

'''Projete uma função que receba como entrada uma string e um número natural n e crie uma nova
string repetindo a string de entrada n vezes (suponha que o operador * não está disponível).'''

def repetidor (texto,n):
    '''
    >>> repetidor("a", 3)
    'aaa'
    >>> repetidor("ab", 2)
    'abab'
    >>> repetidor("", 5)
    ''
    >>> repetidor("xyz", 0)
    ''
    >>> repetidor("!", 1)
    '!'
    >>> repetidor("ab", 1)
    'ab'
    >>> repetidor("a", 10)
    'aaaaaaaaaa'
    '''
    res = ''
    for i in range(n):
        res = res + texto
    
    return res

'''rojete uma função que converta um número natural para uma string. Por exemplo, para o número
4561 a saída deve ser a string '4561' (suponha que a função str não está disponível). Dica: faça
divisões sucessivas por 10.'''

def converte (numero):
    referencia  = '0123456789'
    res = ''
    aux = numero
    divisoes = 0    
    while aux > 10:
            aux = aux // 10
            divisoes = divisoes + 1
    for a in range(0,10):
            if aux == a:
                res = res + referencia[a]
    while divisoes != divisoes + 1:
        numero - (aux ** divisoes)
        for a in range(0,10):
            if numero == a:
                res = res + referencia[a]

    return
'''rojete uma função que receba um número inteiro positivo n, e crie a matriz identidade In, com n
linhas e n colunas, com todos os elementos da diagonal principal (elementos com o mesmo índice)
iguais a 1 e os demais elementos iguais a 0.'''

def identidade (n):
    '''
    >>> identidade(1)
    [[1]]

    >>> identidade(2)
    [[1, 0], [0, 1]]

    >>> identidade(4)
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    '''
    matriz = []
    for i in range(n):
        for i in range(n):
            linha = [0]*n
        matriz.append(linha)
    for i in range(n):
        matriz[i][i]=1
    
    return matriz

'''rojete uma função que encontre os índices de todas as linhas de uma matriz cuja a soma dos elementos
é zero'''

def zero (matriz:list):
    '''
    >>> zero([[1, -1, 0], [0, 0, 0], [2, -2, 0], [1, 2, 0]])
    [0, 1, 2]

    >>> zero([[0, 0], [0, 0]])
    [0, 1]

    >>> zero([[1, 2, 3], [4, 5, -9]])
    [1]

    >>> zero([])
    []

    >>> zero([[1], [2], [3]])
    []
    '''
    res = []
    linhas = len(matriz)
    for n in range(linhas):
        soma = 0
        for i in matriz[n]:
            soma = soma + i 
        if soma == 0:
            res.append(n)
    return res


'''Projete uma função que encontre os índices de todas as colunas de uma matriz cuja a soma dos
elementos é zero'''


def coluna_zero(matriz:list):
    res = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    for n in range(colunas):
        soma = 0
        for i in range(linhas):
            soma = soma + matriz[i][n] 
        if soma == 0:
            res.append(n)
    return res   
