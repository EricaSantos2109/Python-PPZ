#Exercicio 1. Entre com dois números.
a = int(input('Digite o primeiro:  '))
b = int(input('Digite o segundo: '))
print (a + b)

#Exercicio 2. Metros a ser convertido a milimetros
metro=int(input("entre com um valor em metros para ser convertido em milimetros: "))
print(metro*1000)

#Exercicio 3. Calculo em segundos
dias = int(input("Entre com o número de dias: "))
horas = int(input("Entre com as horas: "))
minutos = int(input("Entre com o total de minutos: "))
segundos = int(input("Entre com o total de segundos: "))
total = (dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos)
print("total: ", total) 

#Exercicio 4. Aumento de salário
salario = int(input("Entre com o valor do salário:"))
aumento = int(input("Entre com o valor do aumento:"))
novo = int(salario + (salario * aumento /  100))
print("O salário R$ %s teve um aumento de %a per cento " %(salario, aumento))
print("O novo salário será  %.1f " %(novo))

#Exercicio 5. Solicitação de desconto
produto = int(input("Entre com o valor do produto: "))
desconto = int(input("Entre com o valor do desconto: "))
print(( produto * desconto) / 100)

#Exercicio 6. Calculo do tempo de viagem
distancia = int(input("Entre com a distância a percorrer (km): "))
velocidade = int(input("Entre com a velocidade média (km/h): "))
print("A viagem terá duração de %.1f hora(s)" %(distancia / velocidade))

#Exercicio 7. Conversão de temperatura em Fahrenheit
celsius = int(input("Entre com a temperatura em Celsius: "))
fah = 9 * (celsius / 5) + 32
print("A temperatura em Fahrenheit é %.1f: " %(fah))

#Exercicio 8. Conversão de temperatura em Celsius
fah = int(input("Entre com  a temperatura em Fahrenheit: "))
celsius = (fah - 32) * 5 / 9
print(" A temperatura em Celsius é %.1f: " %(celsius))

#Exercicio 9. Valor do preço a pagar do carro
km =  int(input("km: "))
dias = int(input("dias: "))
total = km * 0.15 + dias * 60
print("Preço: %.2f " %total)

#Exercicio 10. Vida de fumante
anos = int(input("Entre com a quantidade de anos que você fuma: "))
dia = int(input("Entre com a quantidade cigarros fumados por dia: "))
total = (dia * 365) * anos
perdido = (total * 10) / 24
print("A quantidade de dias a menos de vida será de: ", perdido)

#Exercicio 11. Converter valores numericos para string
print(len(str(2**1000000)))
