def convertepara5(texto:str)->str:
    '''
    >>> convertepara5("malbarnboafasfoa")
    malba
    >>> convertepara5("ffdsf")
    ffdsf
    >>> convertepara5("f")
    f    
    '''
    if len(texto)==5:
        print(texto)

    elif len(texto)>5:
        print(texto[0:5])

    else:
        print(texto[0:]+(5-(len(texto)))*" ")
    
    
    return


def negativo_positivo_nulo(n:int)->int:
    '''
    >>> negativo_positivo_nulo(-1)
    -1
    >>> negativo_positivo_nulo(10)
    1
    >>> negativo_positivo_nulo(0)
    0
    '''
    
    
    if n>0:
        print(1)
    elif n<0:
        print(-1)
    else:
        print(0)

    return           


def esta_no_intervalo(min:int,max:int,valor:int)->int:
    '''
    >>> esta_no_intervalo(10,100,59)
    59
    >>> esta_no_intervalo(10,100,5)
    10
    >>> esta_no_intervalo(10,100,-5)
    10
    >>> esta_no_intervalo(-10,100,1)
    1
    >>> esta_no_intervalo(-100,-10,5)
    -10
    >>> esta_no_intervalo(-200,-100,-105)
    -105
    '''
    if min<=valor<=max:
        print(valor)
    elif valor>max:
        print(max)
    else:
        print(min)
    return


def quanto_rende(n:int):
    '''
    >>> quanto_rende(1000)
    100.0
    >>> quanto_rende(2500)
    300.0
    >>> quanto_rende(10000)
    1300.0
    '''
    if n<=2000:
        return round(n*110/100,2)-n
    elif 2000<n<=5000:
        return round(n*112/100,2)-n
    else:
        return round(n*113/100,2)-n
    

def quanto_rende2anos(a:int):
    '''
    >>> quanto_rende2anos(1000)
    210.0
    >>> quanto_rende2anos(2500)
    636.0
    >>> quanto_rende2anos(10000)
    2769.0
    '''
    um_ano=quanto_rende(a)+a
    if um_ano<=2000:
        print(round(um_ano*110/100,2)-a)
    elif 2000<um_ano<=5000:
        print(round(um_ano*112/100,2)-a)
    else:
        print(round(um_ano*113/100,2)-a)
    return

def e_duplicada(a:str):
    '''
    >>> e_duplicada("oioi")
    True
    >>> e_duplicada("oi-oi")
    True
    >>> e_duplicada("oiaoi")
    False
    >>> e_duplicada("eusou-eusou")
    True
    
    '''
    n=len(a)
    if n%2==0:
        print(a[0:(n//2)]==a[(n//2):])
    elif a[n//2]=='-':
        print(a[0:(n//2)]==a[(n//2+1):]) 
    else:
        print(False)
    return

def meu_nivel(nivel_atual:int,horas_jogadas:int):
    '''
    >>> meu_nivel(5,10)
    10
    >>> meu_nivel(14,0)
    10
    >>> meu_nivel(5,20)
    12
    >>> meu_nivel(21,13)
    25
    >>> meu_nivel(25,10)
    25
    >>> meu_nivel(2,0)
    0
    
    '''
    if nivel_atual<25:
        if 4<=horas_jogadas<=5:
            nivel_final=nivel_atual
        elif horas_jogadas<4:
            nivel_final=nivel_atual-(4-horas_jogadas)
            if nivel_final<0:
                print(0)
            else:
                print(nivel_final)
        else:
            nivel_final=nivel_atual+min((horas_jogadas-5)*1,7)
            if nivel_final<=25:
                print(nivel_final)
            else:
                print(25)
    else:
        print(25)
    
    return
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



