
# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = 16
votar = int(input("Digite sua idade: "))

if votar >=16:
    print("Você já tem idade para votar!")
else:
    print("Você ainda não tem idade para votar!") 