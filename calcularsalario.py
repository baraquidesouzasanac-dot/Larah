"""
salario_bruto = float(input("Digite o salário bruto: "))
qtd_horas_extra_diurna = float(input("Digite a quantidade de horas extras diurnas: "))
qtd_horas_extra_dom_fer = float(input("Digite a quantidade de horas extras dom/fer: "))

valor_hora_extra= float(salario_bruto/220)
valor_hora_extra_diurna = float(qtd_horas_extra_diurna * valor_hora_extra * 1.5)
valor_hora_extra_dom_fer = float(qtd_horas_extra_dom_fer * valor_hora_extra * 2)

if salario_bruto <= 1621.00:
    inss= salario_bruto * 0.075
elif salario_bruto <= 2902.84:
    inss= salario_bruto * 0.09
elif salario_bruto <= 4351.27:
    inss= salario_bruto * 0.12
else:
    inss= float(salario_bruto*0.14)

print("salário bruto: R$", salario_bruto)
print("Valor das horas extras diurnas: R$", valor_hora_extra_diurna)
print("Valor das horas extras dom/fer: R$", valor_hora_extra_dom_fer)
print("Valor do INSS: R$", inss)
salario_liquido = salario_bruto + valor_hora_extra_diurna + valor_hora_extra_dom_fer - inss
print("Salário líquido: R$", salario_liquido)
"""

