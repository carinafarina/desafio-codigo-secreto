#Missão 3: Recuperando o Sistema de Notas 📊
#As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."  


notas = int(input("Insira a sua nota: "))

if notas > 90 or notas <100:
    print("Parabéns, você tirou A!")
elif notas > 80 or notas <89:  
    print("Muito bem, você tirou B.")  
elif notas > 70 or notas <79:  
    print("Bom trabalho, você tirou C.")    
elif notas > 0 or notas <69:  
    print("Fique atento, você tirou D.")
elif notas <60:  
    print("Estude um pouco mais, você tirou F.")           
 

    


