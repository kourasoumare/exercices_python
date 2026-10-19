produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# Calcul du total HT puis TTC
total_ht = prix_ht * quantite
total_ttc = total_ht + (total_ht * taux_tva)

print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")

# Le prix arrive maintenant sous forme de texte : on le convertit puis on refait le calcul
prix_texte = "19.90"
prix_ht_converti = float(prix_texte)
total_ht_converti = prix_ht_converti * quantite
total_ttc_converti = total_ht_converti + (total_ht_converti * taux_tva)

print(f"{quantite} x {produit} : {total_ttc_converti:.2f} euros TTC")