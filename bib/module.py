from traceback import print_tb


# Function 1 - Granulção - Start

def recebe_metros():
     return float(input("Digite um valor em metros: "))   

def metros_para_centimetros(m):
    return m * 100

def exercicio_1_function():
    metros = recebe_metros()
    centimetros = metros_para_centimetros(metros)
    print(f"{metros} metros equivalem a {centimetros} centímetros.")  

# Funciton 1 - End

# Function 2 - Start

def input_salario_hora():
    return float(input("Quanto você ganha por hora? (Sómente núnmeros) "))

def input_horas_trabalhadas():
    return float(input("Quantas horas você trabalha por mês? "))

def calcula_salario(salario_hora, horas_trabalhadas):
    return salario_hora * horas_trabalhadas

def exercicio_2_function():
    salario_hora = input_salario_hora()
    horas_trabalhadas = input_horas_trabalhadas()
    salario = calcula_salario(salario_hora, horas_trabalhadas)
    print(f"Seu salário mensal é de R$ {salario:.2f}")

# Function 2 - End
 
# Function 3 - Start

def input_fahrenheit():
    return float(input("Digite a temperatura em graus fahrenheit: "))

def calcula_fahrenheit_para_celsius(fahrenheit):
    return (5 * (fahrenheit - 32) / 9)

def exercicio_3_function():
    fahrenheit = input_fahrenheit()
    celsius = calcula_fahrenheit_para_celsius(fahrenheit)
    print(f"A temperatura em graus Celsius é: {fahrenheit}F em Celsius é {celsius:.2f}")

# Function 3 - End

# Function 4 - Start

def input_altura():
    return float(input("Minha altura é (m): ")) 

def input_peso():
    return float(input("Meu peso é de (kg):"))

def calcula_imc(peso, altura):
    return peso / (altura ** 2)

def exercicio_4_function():
    alt = input_altura()
    peso = input_peso()
    imc = calcula_imc(peso, alt)
    print('O IMC desta pessoa é de {:.2f}'.format(imc))

# Function 4 - End 

# Function 5 - Start

def input_peso_peixe():
    return float(input("Peso total dos peixes (KG): "))

def calcula_peso_excedente(peso, limite):
    return peso - limite

def calcula_multa(peso_excedente, multa):
    return peso_excedente * multa

def exercicio_5_function():
    limite = 30
    multa = 3.00
    pesoExcedente = 0
    peso_peixe = input_peso_peixe()
    if peso_peixe > limite:
        pesoExcedente = calcula_peso_excedente(peso_peixe, limite)
        multa = calcula_multa(pesoExcedente, multa)
        print("Peso acima de:", limite,"kg. Multado em R$", multa,"pelo excesso de: ", pesoExcedente,"kg.")
    else:
        print("Peso dos peixes dentro do limite. Sem multas para você Zé Papo-de-Pescador")

# Function 5 - End

# Function 6 - Start
def calcula_imposto(salario, porcentagem):
    return salario * porcentagem

def exercicio_6_function():
    salario_hora = input_salario_hora()
    horasTrabalhadas = input_horas_trabalhadas()

    salario = calcula_salario(salario_hora, horasTrabalhadas)
    imposto = calcula_imposto(salario, 0.11)
    imp_inss = calcula_imposto(salario, 0.08)
    descontos = imposto + imp_inss
    salario_liquido = salario - descontos

    print("Seu salário bruto é R$ {:.2f}".format(salario))
    print("Seu salário líquido é R$ {:.2f}".format(salario_liquido))
    print("Você pagou R$ {:.2f} de imposto".format(imposto))
    print("Você pagou R$ {:.2f} de INSS".format(imp_inss))

# Function 6 - End
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






# Teste de retorno

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