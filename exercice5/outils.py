def convertir_note(texte):
    texte = texte.replace(",", ".")
    try: 
      return float(texte)
    except ValueError:
        return None

def moyenne(valeurs):
    return sum(valeurs) / len(valeurs) if valeurs else None

def mention(note):
    if note is None:
        return "Aucune note"
    elif note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"