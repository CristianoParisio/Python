def lernotas():
    n=float(input('Digite uma nota para o aluno: '))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="") # o comando end="" faz com que as impressão seja na mesma linha
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
        
a = lernotas()
b = lernotas()
resultado(a, b)
    