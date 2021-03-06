#METODI STATICI
#funzioni nella classe perché hanno correlazione con essa ma non ne sono dirett collegati
#non serve oggetto per richiamarli
#restit info sul codice
class Persona:
    
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
        
    @staticmethod
    def info_prog(): #non passa nè class nè self
        info = """
        Nome: Persona
        Creato da PYMyke
        Sito: www.programmareinpython.it
        Commenti: 
        Linguaggi: Python"""
        return info
    
    @classmethod 
    def from_string (cls, stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split("-")
        return cls(nome, cognome, età, residenza, *args)
    
    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return "Studente"
        else:
            return "Insegnante"

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda
    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")

        scelta = input("Cosa Desideri Modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        elif scelta == "2":
            self.cognome = input("Nuovo cognome --> ")
        elif scelta == "3":
            self.età = input("Nuovo età --> ")
        elif scelta == "4":
            self.residenza = input("Nuovo residenza --> ")
        
class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio
        
    #DUNDER METHODS
    #metodi predefiniti, non chiamati direttamente da noi
    #per es unire dati di più studenti
    def __add__ (self, other):
        return self.nome + " " + other.cognome

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso Di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print("Corso Aggiornato")
        
    #DUNDER STR
    #per rappresentazione oggetti leggibile
    def __str__(self):
        return f"Lo studente {self.nome} {self.cognome} studia {self.corso_di_studio}"

    #DUNDER REPR
    #esaustivo e non ambiguo, permette di ricreare oggetto da stringa che restituisce
    def __repr__(self):
        return f"Studente('{self.nome}', '{self.cognome}', {self.età}, '{self.residenza}', '{self.corso_di_studio}')"
        
#si può accedere a METODO STATICO senza aver creato nessun oggetto
print(Persona.info_prog())

stud1 = Studente("Peter", "Malkovich", 55, "Parigi", "Psicologia")
stud2 = Studente("John","Parker", 18, "New York", "Fisica")
print(stud1 + stud2)
print(stud2 + stud1)
print(stud1) #senza str solo info
#o print(str(stud1))
print(repr(stud2)) #raprresentazione repr perette di ricreare oggetto

