# a partir d'une variable temperature afficher gel sous 0 froid sous 15 doux sous 25 sinon chaud

 
temperatures = [-3, 0, 15, 31]

for temperature in temperatures:
    if temperature < 0:
        categorie = "gel"
    elif temperature < 15:
        categorie = "froid"
    elif temperature < 25:
        categorie = "doux"
    else:
        categorie = "chaud"
    print(f"{temperature} °C : {categorie}")

# Années bissextiles
annees = [2024, 1900, 2000]

for annee in annees:
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")
   
