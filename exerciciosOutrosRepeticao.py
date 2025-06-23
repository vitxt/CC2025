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


    >>> nova_lista([10, 20, 30], -1, 25)
    [10, 20, 25, 30]

    >>> nova_lista([], 0, 100)
    [100]

    >>> nova_lista([10, 20, 30], -4, 5)
    [5, 10, 20, 30]
    '''
    
    res = []
    if i >= 0:
        for n in range(0,len(lst)):
            if n == i:
                res.append(n)
            else:
                res.append(lst[n])
    else:
        

    
    return res