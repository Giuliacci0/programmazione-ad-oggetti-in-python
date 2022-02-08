class Persona:
    
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")
            
class Impiegato(Persona):
    pass

class Medico(Persona):
    pass

#      Siamo già in grado di istanziare sia Studente che Insegnante senza aver ancora scritto nulla al 
#      loro interno, e questo  perché stanno ereditando attributi e metodi da Persona

impiegato_unp = Impiegato("Py", "Mike", 24, "Casa Dello Studente")
medico_uno = Medico("Mario", "Rossi", 33, "Viale Roma 32")

print(impiegato_unp.scheda_personale())
print(medico_uno.scheda_personale())




class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
    #super fa gestire nome cognome età residenza da  metodo init classe genitore
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio
        
    #overwriting di metodo della classe per sottoclassi:
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso: {self.corso_di_studio}\n"""
        return super().scheda_personale() + scheda
    
    def modifica_corso(self, corso):
        self.corso_di_studio = corso

class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Insegnamenti: {self.materie}\n"""
        return super().scheda_personale() + scheda
    def aggiungi_insegnamento(self, materia):
        self.materie.append(materia)
    
studente_uno = Studente("Py", "Mike", 24, "Casa Dello Studente", "Informatica")
insegnante_uno = Insegnante("Mario", "Rossi", 33, "Viale Roma 32", ["Python", "OOP"])
studente_uno.modifica_scheda()
studente_uno.modifica_corso("OOP")
insegnante_uno.aggiungi_insegnamento("Security")
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())
