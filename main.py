from detector_de_mutantes import isMutant
from generador import generador_de_dna

if __name__ == "__main__":
    mutante = False
    contador = 0
    while not mutante:
        mutante = isMutant(generador_de_dna())
        print(mutante)
        contador += 1
    print(f"la persona numer {contador} es mutante")
