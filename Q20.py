# Possibilidade de resposta para a questão 20 da lista do Malbarbo.
# Essa função retorna o maior dos parâmetros -float-  recebidos.

def qual_maior(a: float, b: float) -> float:
    return (a>b and a) or b

# Explicação presente abaixo, caso seja necessária.
# Note que, caso a>b = FALSE, o Python não retorna nem a>b, nem "a", pois este 
# está vinculado a uma informação falsa por meio de um "and", mas retona o "b",
# que, nesse caso, é o maior número. Outrossim, considerando a>b = TRUE,
# o programa retornará o valor de a, nesse caso o maior número, omitirá 
# o resultado de a>b e não retornará o b, devido ao funcionamento do "or"
# ignorar o segundo operando caso o primeiro já seja TRUE.
