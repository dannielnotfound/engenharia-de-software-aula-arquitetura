from traceback import print_tb


def exercicio_1_function():
    meters = float(input("Digite um valor em metros: "))  
    centimenters = meters * 100  
    print(f"{meters} metros equivalem a {centimenters} centímetros.")  

def exercicio_2_function():
    salario_hora = float(input("Quanto você ganha por hora? (Sómente núnmeros) "))
    horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
    salario = salario_hora * horas_trabalhadas
    print(f"Seu salário mensal é de R$ {salario:.2f}")

def exercicio_3_function():
    fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))
    celsius = (5 * (fahrenheit - 32) / 9)
    print(f"A temperatura em graus Celsius é: {fahrenheit}F em Celsius é {celsius:.2f}")

def exercicio_4_function():
    alt = float(input("Minha altura é (m): ")) 
    peso = float(input("meu peso e de (kg)"))
    imc = peso / (alt ** 2)
    print('O IMC desta pessoa é de {:.2f}'.format(imc))

def exercicio_5_function():
    limite = 30
    multa = 3.00
    pesoExcedente = 0
    peso = float(input("Peso total dos peixes (KG): "))
    if peso > limite:
        pesoExcedente = peso - limite
        multa = pesoExcedente * multa
        print("Peso acima de:", limite,"kg. Multado em R$", multa,"pelo excesso de: ", pesoExcedente,"kg.")
    else:
        print("Peso dos peixes dentro do limite. Sem multas para você Zé Papo-de-Pescador")

def exercicio_6_function():
    salario_hora = float(input("Quantos reais você ganha por hora? "))
    horasTrabalhadas = float(input("Quantas horas você trabalha por mês? "))

    salario = salario_hora * horasTrabalhadas
    imposto = salario * 0.11
    imp_inss = salario * 0.08
    descontos = imposto + imp_inss
    salario_liquido = salario - descontos

    print("Seu salário bruto é R$ {:.2f}".format(salario))
    print("Seu salário líquido é R$ {:.2f}".format(salario_liquido))
    print("Você pagou R$ {:.2f} de imposto".format(imposto))
    print("Você pagou R$ {:.2f} de INSS".format(imp_inss))

def exercicio_7_function():
    latas = 80 
    t_latas = 18 
    area = float(input("Informe o tamanho da área que será pintada (m²): "))

    litros = area / 3
    latasUsadas = litros / t_latas
    if litros % t_latas > 0:
        latasUsadas += 1
    total = latasUsadas * latas
    print(f"Você precisará de {latasUsadas:.0f} lata(s) de tinta. Total de R$ {total:.2f}.")


def exercicio_1():
    print('\n')
    print("Exercicio 1 - \n")
    print("#1. Crie um algoritmo que receba um valor em metros e converta para centímetros\n")
    return exercicio_1_function() 

def exercicio_2():
    print('\n')
    print("Exercicio 2 - \n")
    print("#2. Crie um algoritmo que pergunte quanto você ganha por hora e o número de horas que você trabalha por mês, o algoritmo deve calcular e mostrar qual seu salário naquele mês. \n")
    return exercicio_2_function()

def exercicio_3():
    print('\n')
    print("Exercicio 3 - \n")
    print("#3. Crie um algoritmo que receba uma temperatura em Fahrenheit e converta para Celsius\n")
    return exercicio_3_function()
    
def exercicio_4():
    print('\n')
    print("Exercicio 4 - \n")
    print("#4. Crie um algoritmo que receba a altura e o peso de uma pessoa e mostre seu Índice de Massa Corporal (IMC), utilizando a seguinte fórmula:\n")
    return exercicio_4_function()

def exercicio_5():
    print('\n')
    print("Exercicio 5 - \n")
    return exercicio_5_function()

def exercicio_6():
    print('\n')
    print("Exercicio 6 - \n")
    return exercicio_6_function()

def exercicio_7():
    print('\n')
    print("Exercicio 7 - \n")
    return exercicio_7_function()