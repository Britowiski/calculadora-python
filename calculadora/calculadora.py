import math

def calculadora():
    operacao = input('selecione o tipo de operação: +, -, *, /, **, //(raiz quadrada) : \n' )
    num1 = input('digite um número: ')
    num2 = input('digite outro número: ')

    if operacao == "+":
        resultado_soma = eval(num1) + eval(num2)
        print(resultado_soma)
    elif operacao == "-":
        resultado_subtracao = eval(num1) - eval(num2)
        print(resultado_subtracao)
    elif operacao == "*":
        resultado_mult = eval(num1) * eval(num2)
        print(resultado_mult)
    elif operacao == "/":
        resultado_div = eval(num1) / eval(num2)
        print(resultado_div)
    elif operacao == "**":
        resultado_potencia = eval(num1) ** eval(num2)
        print(resultado_potencia)
    elif operacao == "//":
        raiz_1 = math.sqrt(eval(num1))
        raiz_2 = math.sqrt(eval(num2))
        print(raiz_1, raiz_2)
    else:
        print("digite um número ou uma operação válida")
        


calculadora()