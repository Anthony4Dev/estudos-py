
"""
Security = chave
5ecur1ty = senha

hex

1=1
2=2
3=3
4=4
5=5
6=6
7=7
8=8
9=9
10=A
11=B
12=C
13=D
14=E
15=F



chave = input("Digite como você quer a sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "@"
    elif letra in "Mm":
        senha = senha + "%"
    elif letra in "Nn":
        senha = senha + "!"
    else: senha = senha + letra
print(senha)
"""
### Começo dos estudos

""" para ver o numero de caracteres de uma frase
print("Hello World !")
x = 5 
y = "Hello World !"

print(len(y))"""