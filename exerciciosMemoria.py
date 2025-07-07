def soma(lst:list)->list:
    '''
    Projete uma função que modifique uma lista de números somando um valor n a cada um dos seus
    elementos.
    
    >>> soma([1,2,3,4,5])
    [2, 3, 4, 5, 6]
    '''
    for i in range(len(lst)):
        lst[i]=lst[i]+1
    return lst

def strings(lst:list)->list:
    '''
    Projete uma função que modifique uma lista de strings deixando todas com o mesmo tamanho. Adi-
    ciona espaços em branco ao final das strings se necessário.
    
    >>> strings(['oioioi', 'oioi', 'oi'])
    ['oioioi', 'oioi  ', 'oi    ']
    '''
    maior_str = 0
    for i in range(len(lst)):
        if len(lst[i]) > maior_str:
            maior_str = len(lst[i])
    
    for i2 in range(len(lst)):
        lst[i2] = lst[i2] + ' '*(maior_str - len(lst[i2]))

    return lst

def newLista(a:list,b:list)->list:
    '''
    Projete uma função que receba duas listas como parâmetro e modifique a primeira lista adicionando
    todos os elementos da segunda lista no final da primeira.
    >>> a = [1,2,3,4]
    >>> b = [4,3,2,1]
    >>> newLista(a,b)
    [1, 2, 3, 4, 4, 3, 2, 1]
    '''
    for i in range(len(b)):
        a.append(b[i])
    return a

def insere(lst:list,index:int,valor):
    '''
    Projete uma função que receba como parâmetros uma lista, um índice i e um valor v, e modifique a
    lista inserindo o valor v no índice i. Dica: veja o exemplo insere_ordenado.

    >>> lista = [1 , 2, 3, 4, 5]
    >>> insere(lista,0,0)
    [0, 1, 2, 3, 4, 5]

    >>> a = [10, 20, 30]
    >>> insere_em(a, 15, 1)
    >>> a
    [10, 15, 20, 30]

    >>> b = []
    >>> insere(b, 0, 'a')
    ['a']

    >>> c = [1, 2, 3]
    >>> insere(c, 4, 4)
    [1, 2, 3, 4]

  
    '''
    lst.append(valor)
    i = len(lst) - 1
    while i != 0:
        if lst[index]!=valor:
            aux = lst[i]
            lst[i] = lst[i-1]
            lst[i-1] = aux
        i = i -1
    return lst