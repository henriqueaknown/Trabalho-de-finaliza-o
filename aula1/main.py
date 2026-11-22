
########
# IMPORTS
########
import math
import time

########
# FUNÇÕES
########


def calcular_tempo_chuveiro(tempo_espera, tempo_banho, banhos_dia):
    tempo_total = (tempo_espera + tempo_banho) * banhos_dia
    return tempo_total



def calcular_energia(consumo_kwh):
    pontos = consumo_kwh / 150
    return pontos


def calcular_gasolina(litros_gasolina):
    pontos = litros_gasolina / 50
    return pontos


def calcular_agua(tempo_chuveiro):
    pontos = tempo_chuveiro / 30
    return pontos


def calcular_planetas(energia, gasolina, agua):
    pontuacao_total = energia + gasolina + agua

    planetas = pontuacao_total / 3

    return round(planetas, 2)


########
# PROGRAMA PRINCIPAL
########

def main():

    print("==========================")
    print("       🌎 ECODICAS")
    print("==========================")

    print("\nResponda às perguntas abaixo.")

    # Energia
    energia = float(input("\nQuantos kWh você consome por mês, em média? "))

    # Transporte
    gasolina = float(input("Quantos litros de gasolina consome por mês? "))

    # Água
    espera = float(input("Quantos minutos espera o chuveiro aquecer? "))
    banho = float(input("Quantos minutos dura seu banho? "))
    banhos = int(input("Quantos banhos toma por dia? "))

    tempo_chuveiro = calcular_tempo_chuveiro(
        espera, banho, banhos
    )

    # Cálculos
    pontos_energia = calcular_energia(energia)
    pontos_gasolina = calcular_gasolina(gasolina)
    pontos_agua = calcular_agua(tempo_chuveiro)

    planetas = calcular_planetas(
        pontos_energia,
        pontos_gasolina,
        pontos_agua
    )

    print("\n==========================")
    print("       RESULTADO")
    print("==========================")

    print(f"Pontuação de energia: {pontos_energia:.2f}")
    print(f"Pontuação de gasolina: {pontos_gasolina:.2f}")
    print(f"Pontuação de água: {pontos_agua:.2f}")

    print(f"\nVocê utiliza o equivalente a {planetas} Terras!")


main()

