
pontos = 0

print("================================")
print("       🌎 QUIZ ECODICAS")
print("================================")
print("Responda às 10 perguntas!")
print()

# Pergunta 1
print("1 - O que causa o aquecimento global?")
print("A) Gases do efeito estufa")
print("B) Fases da Lua")
print("C) Movimento das ondas")

resposta = input("Resposta: ").upper()

if resposta == "A":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era A.")

print()

# Pergunta 2
print("2 - Qual atividade aumenta a emissão de CO2?")
print("A) Plantar árvores")
print("B) Queimar combustíveis fósseis")
print("C) Reciclar papel")

resposta = input("Resposta: ").upper()

if resposta == "B":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era B.")

print()

# Pergunta 3
print("3 - Qual é uma consequência das mudanças climáticas?")
print("A) Aumento de eventos climáticos extremos")
print("B) Fim da gravidade")
print("C) Diminuição da luz solar")

resposta = input("Resposta: ").upper()

if resposta == "A":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era A.")

print()

# Pergunta 4
print("4 - Qual atitude ajuda o meio ambiente?")
print("A) Desperdiçar água")
print("B) Jogar lixo nos rios")
print("C) Economizar energia")

resposta = input("Resposta: ").upper()

if resposta == "C":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era C.")

print()

# Pergunta 5
print("5 - Qual gás é um dos principais responsáveis pelo efeito estufa?")
print("A) Oxigênio")
print("B) Dióxido de carbono (CO2)")
print("C) Hélio")

resposta = input("Resposta: ").upper()

if resposta == "B":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era B.")

print()

# Pergunta 6
print("6 - O desmatamento contribui para:")
print("A) Aumentar a absorção de CO2")
print("B) Reduzir a temperatura global")
print("C) Agravar as mudanças climáticas")

resposta = input("Resposta: ").upper()

if resposta == "C":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era C.")

print()

# Pergunta 7
print("7 - Qual fonte de energia é renovável?")
print("A) Energia solar")
print("B) Carvão mineral")
print("C) Petróleo")

resposta = input("Resposta: ").upper()

if resposta == "A":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era A.")

print()

# Pergunta 8
print("8 - Qual atitude ajuda a diminuir a poluição?")
print("A) Queimar lixo")
print("B) Utilizar transporte público")
print("C) Jogar plástico no mar")

resposta = input("Resposta: ").upper()

if resposta == "B":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era B.")

print()

# Pergunta 9
print("9 - O que podemos fazer para evitar o desperdício de água?")
print("A) Deixar a torneira aberta")
print("B) Tomar banhos muito longos")
print("C) Fechar a torneira ao escovar os dentes")

resposta = input("Resposta: ").upper()

if resposta == "C":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era C.")

print()

# Pergunta 10
print("10 - Qual é a importância das árvores?")
print("A) Absorver CO2 e ajudar no equilíbrio ambiental")
print("B) Aumentar a poluição")
print("C) Impedir a formação de nuvens")

resposta = input("Resposta: ").upper()

if resposta == "A":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto! A resposta era A.")

# Resultado final
print()
print("================================")
print("          RESULTADO")
print("================================")
print("Sua pontuação foi:", pontos, "/ 10")

if pontos == 10:
    print("Excelente! Você é um especialista ambiental!")
elif pontos >= 7:
    print("Muito bem! Você conhece bastante sobre o meio ambiente!")
elif pontos >= 4:
    print("Bom trabalho! Continue aprendendo!")
else:
    print("Continue estudando! Cada atitude faz a diferença!")

print("Obrigado por participar!")