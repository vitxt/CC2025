carrinhoDeCompras = {

}


def add():
        a = input("Qual item deseja adicionar?")
        b = int(input("Qual quantidade deseja adicionar?"))
        carrinhoDeCompras[a] = b
    
def sub():
        a = str(input("Qual item deseja remover?"))
        del carrinhoDeCompras[a]

def visualizar():
        for i,n in carrinhoDeCompras.items():
            print(i,',',n)
    
def atualizar():
        a = input("Qual item deseja atualizar?")
        b = int(input("Qual a nova quantidade?"))
        carrinhoDeCompras[a]=b


a = int
while a !=0:
    opt = int(input("Digite 1 para visualizar o carrinho de compras; \
                    \n Digite 2 para adicionar um item; \
                    \n Digite 3 para remover um item; \
                    \n Digite 4 para atualizar a quantidade de um item; \
                    \n Digite 0 para sair; \
                    \n O que deseja realizar?"))
    if opt == 1:
           visualizar()
    if opt == 2:
           visualizar()
           add()
    if opt == 3:
           visualizar()
           sub()
    if opt ==4:
           visualizar()
           atualizar()
    if opt == 0:
           a = 0