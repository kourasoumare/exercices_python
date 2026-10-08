produit = "Clavier"
prix_ht=19.90
quantite = 3
taux_tva = 0.2
# Calcul du prix total HT
total_ht = prix_ht * quantite
#calcul du prix total TTC
total_ttc = total_ht + (total_ht * taux_tva)

#afficher le prix total arrondi a 2 decimales avec f-string
print(f"Le prix total HT pour {quantite} {produit}(s) est : {total_ht:.2f} ")
print(f"Le prix total TTC pour {quantite} {produit}(s) est : {total_ttc:.2f} ")

prix_texte="19.90"
prix_ht2 = float(prix_texte)
total_ht2 = prix_ht2 * quantite
print(f"Le prix total HT pour {quantite} {produit}(s) est : {total_ht2:.2f} ")