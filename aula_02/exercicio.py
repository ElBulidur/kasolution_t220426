"""
    Em um clube, o valor da entrada varia de acordo com a idade do associado. 
    Os critérios são: 
     Até 17 anos - R$ 50,00; 
     Entre 18 e 59 anos - R$ 60,00; 
     A partir de 60 anos - R$ 20,00. 
    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago. 

"""

assossiado = input("Nome do associado: ")
ingresso = 10
idade = int(input("Idade do assossiado: "))

if idade < 18:
    ingresso = 50
elif idade > 17 and idade < 60:
    ingresso = 60
else:
    ingresso = 20
    
print(f"O assossiado {assossiado}, ira pagar R$ {ingresso:.2f}")

