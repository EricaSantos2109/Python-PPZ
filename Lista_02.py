#Lista 2
#Exercicio 1
a = int(input("Entre com o valor do primeiro lado: "))
b = int(input("Entre com o valor do segundo lado: "))
c = int(input("Entre com o valor do terceiro lado: "))

if a > b + c or b > a + c or c > a + b :
    print("Valores invalidos, não é triangulo")
else:
    if a == b == c:
        print("triangulo equilátero")
    elif a == b or b == c or a == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")

#Exercicio 2
a = int(input("Entre com o ano: "))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

#Exercicio 3
peixe = int(input("Entre com o peso do peixe:"))
if peixe > 50 :
    kilos = peixe - 50
    multa = 4.00
    print("Valor do peixe está acima do apropriado. Valor da multa R$%6.2f" %(kilos * multa))

else:
    print("Sem problemas!")

#Exercicio 4
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
if a >= b and a >= c:
    print("Maior: %d" %a)
elif b >= c:
    print("Maior: %d" %b)
else:
    print("Maior: %d" %c)

#Exercicio 5
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
if a <= b and a <= c:
    print("Menor: %d" %a)
elif b <= c:
    print("Menor: %d" %b)
else:
    print("Menor: %d" %c)

#Exercicio 6
valor = float(input("Valor por hora:"))
horas = int(input("Horas trabalhadas:"))
bruto = valor * horas
i = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - i - inss - sind
print("salario bruto: R$ %10.2f" %bruto)
print("i: R$ %10.2f" %i)
print("inss: R$ %10.2f" %inss)
print("sindicato: R$ %10.2f" %sind)
print("salário líquido: R$ %10.2f" %liquido)


#Exercicio 7
metro = int(input("Entre com o número em metros:"))

if metro % 54 == 0:
    lata = int(metro / 54)
else:
    lata = int(metro / 54) + 1
print(f"Preciso de {lata} latas. Custo de R${lata*80:.2f}")

