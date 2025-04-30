# %%
def e_par(x: int) -> bool:
    return (x % 2) == 0

def tres_digitos(x: int) -> bool:
    return x >= 100 and x <= 999

def termina_z(x: str) -> str:
    return x[-1] == "z"

#Verifica se o caractere do meio e '-'
def meio(frase: str) -> bool:
    caracter: int = (len(frase) // 2)
    return (frase[caracter]) == '-' and ((len(frase)) % 2) == 1

#Hipotenusa dos catetos
def hipotenusa(x:float, y:float):
    return ((x ** 2) + (y ** 2)) ** 0.5

#Recebe dia mes e ano e retorna  ano mes e dia
def data(data:str):
    dia:str = data[:2]
    mes:str = data[3:6]
    ano:str = data[6:10] + '/'
    return str(ano + mes + dia)

#Verifica se o nome é mediano, maior que 3 letras e menor que 8 letras
def nome_med(nome:str) -> bool:
    return len(nome) > 3 and len(nome) < 8

#Retorna a unidade de um numero
def unidade(num:int) -> int:
    return num % 10

#Retorna a dezena
def dezena(num:int) -> int:
    dez1:int = (num % 100)
    return int(str(dez1)[0])

#Retorna a centena
def dezena(num:int) -> int:
    dez1:int = (num % 1000)
    return int(str(dez1)[0])

#Ultimos dois digitos sao zero
def saozero(num:int) -> bool:
    return (str(num))[-2:] == '00'

#Verifica se o primeiro nome é paula
def epaula(nome:str) -> bool:
    return (nome[:5]).lower() == 'paula'

#Verifica se os numeros podem formar um triangulo
def etriang(x:float, y:float, z:float) -> bool:
    return ((x + y) > z) and ((y + z) > x) and ((x + z) > y)

#Verifica se o sobrenome é silva
def esilva(nome:str) -> bool:
    return (nome[-5:]).lower() == 'silva'

#Encontra o maior valor entre dois numeros
def maior_valor(x: float, y:float) -> float:
    return ((x > y) * x) + ((y > x) * y)
# %%
