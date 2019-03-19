#Lista 3
#Exercicio 1
while True:
    nota = float(input("Entre com a nota:"))
    if nota < 0 or nota > 10:
        print("valor invalido")
    else:
        break
print("Ta tudo certo!")

#Exercicio 2
while True:
    nome = str(input("Entre com seu nome: "))
    senha = str(input("Entre com sua senha:"))
    if nome == senha:
        print("Senha invalida!")
    else:
        break
print("Tudo certo!")
    
#Exercicio 3
pop_a = 80000
taxa_a = 0.03
pop_b = 200000
taxa_b = 0.015
anos = 0
while True:
    if pop_a <= pop_b:
        anos = anos + 1
        pop_a = pop_a + (pop_a * taxa_a)
        pop_b = pop_b + (pop_b * taxa_b)
        print(f"População A: {pop_a}")
        print(f"População B: {pop_b}")
        print(f" {anos} passados")
    else:
        break

#Exercicio 4
n = int(input("n: "))
x = 1
a,b = 1,1
while x <= n - 2:
    a,b = b,a+b
    x=x+1
print(b)


#Exercicio 5
a = int(input("a: "))
b = int(input("b : "))
while a%b!=0:
    a,b=b,a%b
print(b)
