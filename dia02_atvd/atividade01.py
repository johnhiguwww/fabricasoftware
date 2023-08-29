"""
Arquivo da pasta "dia02_atvd"
1.crie um programa que receba uma idade e retorne se poder obter carteira de motorista(CNH)

1 - adcione um input
2- crie a função para verificar se pode ou não ter CNH
3- imprima o resultado na tela
"""
while True:
    idade = input("Informe sua idade: ")
    #Se a codição do Try estiver verdadeira ele vai parar o while
    try:
        if int(idade) >= 18:
            print("Você possui a idade correta!\nPode tirar a CNH")
            break
        else:
            print("Você não possui idade!\nNão pode tirar a CNH")
            break
    #Se atingir o "except" ira retornar o While
    except ValueError:
        print('Digite apenas números inteiros ou validos para informar a idade!!!')