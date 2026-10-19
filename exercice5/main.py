from outils import convertir_note, moyenne, mention
notes_brutes = ["12,5", "15" , "abc", "9", "18,25"]

notes_converties = [convertir_note(note) for note in notes_brutes]
notes_valides = [note for note in notes_converties if note is not None]
compter_notes_invalides = len([note for note in notes_converties if note is None])
#print("Notes converties :", notes_converties)
#print("Notes valides :", notes_valides)

moyenne_notes = moyenne(notes_valides)
print(f"Notes ignorées : {compter_notes_invalides}")
print(f"Moyenne : {moyenne_notes:.2f}")
print(f"Mention : {mention(moyenne_notes)}")
