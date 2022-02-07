""" tutorial programmareinpython.it"""
class Studente:
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
    def scheda_personale(self):
        return f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso Di Studi:{self.corso_di_studi}"
studente_uno = Studente("Py", "Mike", "programmazione")
studente_due = Studente("Marta", "Stannis", "scienze politiche")
print(studente_uno)
print(studente_due)
#output di print()= Oggetti di tipo Studente creati dal Modello Generico della Classe Studente, presenti in due allocazioni di Memoria diverse
print(studente_due.scheda_personale())
print(Studente.scheda_personale(studente_uno))
#visualizzano scheda studente