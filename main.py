import csv

dados = list()

while True:

    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    estado = str(input('Digite seu estado: '))
    salario = float(input('Digite seu salário: '))

    dados.append([nome, idade, estado, salario])

    continuar = str(input('Deseja continuar ?[S/N]: ')).lower()
    if continuar != 's':
        break

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Idade', 'Estado', 'Salário'])
    writer.writerows(dados)

print('Dados salvos em data.csv...')
