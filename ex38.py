def obter_maior(numero, numero2, numero3):
    maior = None
    if numero > numero2 and numero > numero3:
        maior = numero
    elif numero2 > numero and numero2 > numero3:
        maior = numero2
    else:
        maior = numero3
    return maior


def dobrar(numero):
    return numero * 2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maiorNum = obter_maior(num1,num2,num3)
print(dobrar(maiorNum))
