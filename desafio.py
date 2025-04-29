def funcao1 (a:int,b:int)->bool:
    c=a-b
    return(c)


def qual_maior (a:int,b:int)->bool:
    return print("O número ",a," é o maior?",funcao1(a,b)>0,"\n O número ",b," é o maior?",funcao1(a,b)<0)


qual_maior(1,2)
qual_maior(0,8)
qual_maior(177,94)
qual_maior(-6,-3)
qual_maior(-2,6)