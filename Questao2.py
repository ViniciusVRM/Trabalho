num = int(input("Digite um número de 4 dígitos para criptografar "))

m = num // 1000%10
c = num // 100%10
d = num // 10%10
u = num // 1%10

n1 = (m+6)%10
n2 = (c+6)%10
n3 = (d+6)%10
n4 = (u+6)%10

t = n1
t1 = n3
n1 = t1
n3 = t

t = n2
t1 = n4
n2 = t1
n4 = t

str(n1)
str(n2)
str(n3)
str(n4)

print("O número criptografado é: %s%s%s%s"%(n1,n2,n3,n4))

num1 = int(input("Digite o número criptografado para descriptografar "))

m1 = num1 // 1000%10
c1 = num1 // 100%10
d1 = num1 // 10%10
u1 = num1 // 1%10

n5 = m1
n5 = (n5+10)-6
tam = len(str(n5))
if(tam>=2):
    n5 = n5%10

n6 = c1
n6 = (n6+10)-6
tam = len(str(n6))
if(tam>=2):
    n6 = n6%10

n7 = d1
n7 = (n7+10)-6
tam = len(str(n7))
if(tam>=2):
    n7 = n7%10

n8 = u1
n8 = (n8+10)-6
tam = len(str(n8))
if(tam>=2):
    n8 = n8%10
 
t = n7
t1 = n5
n7 = t1
n5 = t

t = n8
t1 = n6
n8 = t1
n6 = t

str(n5)
str(n6)
str(n7)
str(n8)

print("O número descriptografado é: %s%s%s%s"%(n5,n6,n7,n8))



















