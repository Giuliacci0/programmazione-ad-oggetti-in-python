class Studente:
    ore_settimanali = 36            # Variabile Di Classe

    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
#si può accedere alla variabile di classe tramite classe o istanza
    def scheda_personale(self):
        return f"""Scheda Studente
Nome:{self.nome}
Cognome:{self.cognome}
Corso Di Studi:{self.corso_di_studi}
Ore Settimanali:{Studente.ore_settimanali}""" #classe

    def schedapersonale(self):
        return f"""Scheda Studente
Nome:{self.nome}
Cognome:{self.cognome}
Corso Di Studi:{self.corso_di_studi}
Ore Settimanali:{self.ore_settimanali}""" #istanza

studente_uno = Studente("Py", "Mike", "programmazione")
studente_due = Studente("Marta", "Stannis", "scienze politiche")

print(studente_uno.scheda_personale())
print(Studente.schedapersonale(studente_due))

#Accedendo alla varibile di classe tramite istanza la si può modificare per ogni istanza:
studente_uno.ore_settimanali += 4

print(studente_uno.schedapersonale()) #40 invece di 36. 
print(studente_due.schedapersonale())

 # per unna Variabile di Classe che rappresenti il numero totale di impiegati o studenti:
 
class Impiegato:
    ore_settimanali = 36
    totale_impiegati = 0

    def __init__(self, nome, cognome, ufficio):
        self.nome = nome
        self.cognome = cognome
        self.ufficio = ufficio
        Impiegato.totale_impiegati += 1

imp_uno = Impiegato("Py", "Mike", "vendite")
imp_due = Impiegato("Marta", "Stannis", "marketing")

print(Impiegato.totale_impiegati)