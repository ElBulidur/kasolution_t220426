# FUNÇÕES

def boas_vindas():
    print("Seja bem vindo")

# def boas_vindas(): print("Seja bem vindo")

# def boas_vindas(): ...

# def boas_vindas(): pass


# NÃO RETORNA

# Sem parametro

def boas_vindas():
    print("Seja bem vindo")
    
# boas_vindas()

# com parametro
def imprimir_numero_mais_10(numero):
    print(numero + 10)
    
# imprimir_numero_mais_10(15)

# com multiparametro
def somar_dois_numeros(numero_1, numero_2):
    print(f"A soma é: {numero_1 + numero_2}")
    
# somar_dois_numeros(10, 20)

# com inferencia
def boas_vindas_ao_usuario(usuario: str):
    print(f"Seja bem vindo(a) {usuario.capitalize()}")
    
# boas_vindas_ao_usuario("julio pereira")

# RETORNA DADOS

# sem parametro
def boas_vindas() -> str:
    return "Seja bem vindo"
    
res = boas_vindas()


# com parametro
def retorna_numero_mais_10(numero) -> int | float | str:
    try:
        numero = int(numero)
    except:
        try:
            numero = float(numero)
        except:
            return "Precisa ser numero"
    
    return numero + 10


# numero = input("digite o numero: ")

# res = retorna_numero_mais_10(numero)

# print( type(res) )
# print( res )

# Função com parametro padrão
def aplicar_desconto(valor, desconto=10):
    valor_desconto = valor * (desconto/100)
    return valor - valor_desconto

res = aplicar_desconto(100, 20)

# print(res)

# ARGS, LISTA DE PARAMENTRO

def somar_carrinho(*args):
    return sum(args)


res = somar_carrinho(15, 42.5, 89, 45, 48, 75)


# KARGS, CHAVES DE PARAMETRO

def calcular_impostos(salario, **impostos):
    
    valor_a_pagar = 0
    
    if impostos.get("ipva"):
        print(f"vai pagar imposto do carro no valor de {impostos.get("ipva")}")
        valor_a_pagar += impostos.get("ipva")
        
    if impostos.get("iptu"):
        print(f"vai pagar imposto da casa no valor de {impostos.get("iptu")}")
        valor_a_pagar += impostos.get("iptu")
        
    print("")
    print(f"Valor total a pagar: {valor_a_pagar}")
    print(f"Valor descontado: {salario - valor_a_pagar}")
        
    

# calcular_impostos(2500, iptu=200, ipva=150, inss=1000)


# print(res)

# PROGRAMAÇÃO FUNCIONAL

def somar_dois_numeros(numero_1, numero_2):
    print(f"A soma é: {numero_1 + numero_2}")
    

# somar_dois_numeros(20, 10)

somar_dois_numeros_funcional =  lambda numero_1, numero_2: numero_1 + numero_2

# print(f"soma com lambda: {somar_dois_numeros_funcional(10, 20)}")