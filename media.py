notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

mediafinal = (notaA + notaB) / 2

if mediafinal >= 7.0:
    print("A média %.1f - APROVADO " % mediafinal) 
    
else:
    print("A média %.1f - REPROVADO " % mediafinal)
    

# # o número na frente do %.1f representa o número de casas decimais o programa
# vai imprimir, se for (2f) vai imprimir (0.00) de for (3f)-(0.000)