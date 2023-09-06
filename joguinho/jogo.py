import random
num = random.randint(1,10)
print("bem vindo ao advinha numero")
print("tente advinhar um numero de 1 a 10")

resposta = input("digite aq:")

if resposta == num :
    print("parabens")
else:
    print("voçe falhou")
    print(f"o numero era :{num}" )