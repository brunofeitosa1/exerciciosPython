nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

print('Media: ',media)
    
if media < 7.0:
    print('Aluno reprovado')
elif media < 10:
    print('Aluno aprovado')
else:
    print('Aprovado com Distinção!')
