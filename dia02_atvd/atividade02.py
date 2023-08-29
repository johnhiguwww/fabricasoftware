"""
2. Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h.
   mostre que ele foi multado. a muita é de 7 R$ por cada km acima do limite
"""
# while True:
#     velocidade = 0
#     velocidade = input("Informe a Velocidade que o carro estava percorrendo: ")
    #Se a codição do Try estiver verdadeira ele vai parar o while
    # try:
    #     if int(velocidade) >= 80 or float(velocidade) >= 80:
    #         print("Multado!!!")
    #         resto_kilometragem = velocidade / 80
    #         multa = resto_kilometragem * 7
    #         print(f"Foi multado no valor de R$ {multa}")
    #         break
    #     else:
    #         print("O Veiculo não ultrapassou a velocidade de 80km")
    #         break
    # #Se atingir o "except" ira retornar o While
    # except ValueError:
    #     print('Digite apenas números!!!')

velocidade = input("Informe a Velocidade que o carro estava percorrendo: ")

velocidade_em_init = 0
try:
    velocidade_em_init = int(velocidade)
except ValueError:
    print("Digite numeros inteiros")
    
if velocidade_em_init > 80:
    print(f"Veículo Multado!!! {velocidade_em_init} Km/h")
    print(f"Multa de R$ {(velocidade_em_init - 80) * 7}")
elif velocidade_em_init == 80:
    print ("Veículo está na velocidade permitida.")
else:
    print (f'A velocidade atual do carro é {velocidade} Km/h, abaixo da velocidade')
