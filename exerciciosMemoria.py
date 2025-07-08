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



def insere(lst:list,valor,index:int):
    '''
    Projete uma função que receba como parâmetros uma lista, um índice i e um valor v, e modifique a
    lista inserindo o valor v no índice i. Dica: veja o exemplo insere_ordenado.

    >>> lista = [1 , 2, 3, 4, 5]
    >>> insere(lista,0,0)
    [0, 1, 2, 3, 4, 5]

    >>> a = [10, 20, 30]
    >>> insere(a,15,1)
    [10, 15, 20, 30]

    >>> b = []
    >>> insere(b,'a',0)
    ['a']

    >>> c = [1, 2, 3]
    >>> insere(c,4,3)
    [1, 2, 3, 4]

  
    '''
    lst.append(valor)
    i = len(lst)-1
    certo = False
    while i > 0 and not certo:
        aux = lst[i]
        if lst[i] == valor and i == index:
            certo = True
        else:
            lst[i]=lst[i-1]
            lst[i-1]=aux
        i = i-1

    return lst

def remove_indice(lst:list,index:int):
    '''Projete uma função que receba como parâmetros uma lista e um índice i e modifique a lista removendo
    o elemento do índice i.
    >>> lst = [7, 1, 8, 9]
    >>> remove_indice(lst, 2)
    [7, 1, 9]


    >>> lst2 = ['a', 'b', 'c', 'd', 'e']
    >>> remove_indice(lst2, 0)
    ['b', 'c', 'd', 'e']

    >>> lst3 = [10, 20, 30]
    >>> remove_indice(lst3, 2)
    [10, 20]

    >>> lst4 = [5]
    >>> remove_indice(lst4, 0)
    []

    '''
    while index < len(lst)-1:
        aux = lst[index]
        lst[index] = lst[index+1]
        lst[index+1]=aux
        index +=1
    lst.pop()
    return lst


def remover_indices_pares(lst:list):
    '''Projete uma função que modifique uma lista removendo todos os elementos que estão em índices pares
    (não utilize uma lista auxiliar)


    >>> lista2 = ['a', 'b', 'c', 'd']
    >>> remover_indices_pares(lista2)
    ['b', 'd']

    >>> lista3 = [10, 20, 30]
    >>> remover_indices_pares(lista3)
    [20]

    >>> lista4 = [100]
    >>> remover_indices_pares(lista4)
    []

    >>> lista5 = []
    >>> remover_indices_pares(lista5)
    []

    >>> lista6 = [1, 2]
    >>> remover_indices_pares(lista6)
    [2]

    >>> lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> remover_indices_pares(lista1)
    [1, 3, 5, 7, 9]
    '''
    a = len(lst)-1
    while a > 0:
        if a % 2 == 0:
            index = a
            while index < len(lst)-1:
                aux = lst[index]
                lst[index] = lst[index+1]
                lst[index+1]=aux
                index +=1
                lst.pop()
        a -=1

    return lst
