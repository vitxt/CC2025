def caracteres_exibidos (mensagem:str,momento:int,numero_caracteres:int):
    
    
    '''
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',4,13)
    ocao de sorve
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',32,13)
    ve 3! Promoca
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',35,13)
    3! Promocao d
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',4,25)
    ocao de sorvetes, pague 2
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',15,25)
    vetes, pague 2 leve 3! Pr
    >>> caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',29,25)
     leve 3! Promocao de sorv
    '''
    if momento<=len(mensagem)-numero_caracteres:
        exibir=mensagem[momento:momento+numero_caracteres]
    else:
        exibir=mensagem[momento:]+' '+mensagem[:numero_caracteres-(len(mensagem)-momento+1)]

    
    
    
    return print(exibir)



caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',4,13)
caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',32,13)
caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',35,13)
caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',4,25)
caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',15,25)
caracteres_exibidos('Promocao de sorvetes, pague 2 leve 3!',29,25)
