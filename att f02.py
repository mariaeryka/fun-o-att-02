# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "O numero é par."
    else:
        return "O numero é ímpar."